from pathlib import Path

from config.gemini_client import client

from models.judge.judge_report import JudgeReport
from models.judge.verificationcase import VerificationCase


class Judge:

    def __init__(self):

        self.client = client

        self.system_prompt = Path(
            "prompts/judge_system_prompt.md"
        ).read_text(encoding="utf-8")

    def build_prompt(
        self,
        case: VerificationCase
    ) -> str:

        return f"""
==========================
PAIR 1 REPORT
==========================

{case.pair1_report.model_dump_json(indent=2)}

==========================
PAIR 2 REPORT
==========================

{case.pair2_report.model_dump_json(indent=2)}

==========================
AUDITOR REPORT
==========================

{case.auditor_report.model_dump_json(indent=2)}
"""

    def analyze(
        self,
        case: VerificationCase
    ) -> JudgeReport:

        prompt = self.build_prompt(case)

        response = self.client.interactions.create(

            model="gemini-3.6-flash",

            input=f"{self.system_prompt}\n\n{prompt}",

            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": JudgeReport.model_json_schema(),
            },
        )

        judge_report = JudgeReport.model_validate_json(
            response.output_text
        )
        return judge_report

    def analyze_batch(
        self,
        cases: list[VerificationCase]
    ) -> list[JudgeReport]:

        outputs: list[JudgeReport] = []

        for case in cases:
            outputs.append(
                self.analyze(case)
            )

        return outputs