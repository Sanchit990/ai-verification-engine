from pathlib import Path

from config.gemini_client import client
from models.agent_output import AgentOutput
from models.pair_consensus_report import PairConsensusReport


class ConsensusEngine:

    def __init__(self):

        self.client = client

        self.system_prompt = Path("prompts/pair2/consensus_system_prompt.md").read_text(encoding="utf-8")

    def build_prompt(self,a1_output: AgentOutput,a2_output: AgentOutput,) -> str:

        return f"""
==================================================
ANALYSIS 1
==================================================

{a1_output.model_dump_json(indent=2)}

==================================================
ANALYSIS 2
==================================================

{a2_output.model_dump_json(indent=2)}
"""

    def analyze(self,a1_output: AgentOutput,a2_output: AgentOutput,) -> PairConsensusReport:

        prompt = self.build_prompt( a1_output,a2_output)

        response = self.client.interactions.create(

            model="gemini-3.6-flash",

            input=f"{self.system_prompt}\n\n{prompt}",

            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": PairConsensusReport.model_json_schema(),
            },
        )

        return PairConsensusReport.model_validate_json(
            response.output_text
        )

    def analyze_batch(self,a1_outputs: list[AgentOutput], a2_outputs: list[AgentOutput],) -> list[PairConsensusReport]:

        reports: list[PairConsensusReport] = []

        for a1, a2 in zip(a1_outputs, a2_outputs):

            reports.append(
                self.analyze(
                    a1,
                    a2
                )
            )

        return reports