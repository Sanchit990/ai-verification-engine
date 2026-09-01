from pathlib import Path

from config.gemini_client import client

from models.judge_report import JudgeReport
from models.pair1 import Pair1Report
from models.pair2 import Pair2Report
from models.auditor_report import AuditorReport


class Judge:

    def __init__(self):

        self.client = client

        self.system_prompt = Path(
            "prompts/judge_system_prompt.md"
        ).read_text(encoding="utf-8")

    def build_prompt(
        self,
        pair1_report,
        pair2_report,
        auditor_report,
    ):

        return f"""
==========================
PAIR 1 REPORT
==========================

{pair1_report.model_dump_json(indent=2)}

==========================
PAIR 2 REPORT
==========================

{pair2_report.model_dump_json(indent=2)}

==========================
AUDITOR REPORT
==========================

{auditor_report.model_dump_json(indent=2)}
"""

    def analyze(self, pair1_report, pair2_report, auditor_report,):

        prompt = self.build_prompt(
            pair1_report,
            pair2_report,
            auditor_report
        )

        response = self.client.interactions.create(

            model="gemini-3.6-flash",

            input=f"{self.system_prompt}\n\n{prompt}",

            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": JudgeReport.model_json_schema(),
            },
        )

        return JudgeReport.model_validate_json(
            response.output_text
        )

    def analyze_batch(
        self,
        pair1_reports,
        pair2_reports,
        auditor_reports,
    ):

        outputs = []

        for p1, p2, audit in zip(
            pair1_reports,
            pair2_reports,
            auditor_reports
        ):

            outputs.append(
                self.analyze(
                    p1,
                    p2,
                    audit
                )
            )

        return outputs