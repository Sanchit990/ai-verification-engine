from pathlib import Path

from config.gemini_client import client

from models.pair1 import Pair1Report
from models.pair2 import Pair2Report
from models.auditor_report import AuditorReport


class Auditor:

    def __init__(self):
        self.client = client

        self.system_prompt = Path(
            "prompts/auditor/auditor_system_prompt.md"
        ).read_text(encoding="utf-8")

    def build_prompt(
        self,
        pair1_report: Pair1Report,
        pair2_report: Pair2Report,
    ) -> str:

        return f"""
==================================================
PAIR 1 REPORT
==================================================

{pair1_report.model_dump_json(indent=2)}

==================================================
PAIR 2 REPORT
==================================================

{pair2_report.model_dump_json(indent=2)}
"""

    def analyze(
        self,
        pair1_report: Pair1Report,
        pair2_report: Pair2Report,
    ) -> AuditorReport:

        prompt = self.build_prompt(
            pair1_report,
            pair2_report,
        )

        response = self.client.interactions.create(
            model="gemini-3.6-flash",
            input=f"{self.system_prompt}\n\n{prompt}",
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": AuditorReport.model_json_schema(),
            },
        )

        return AuditorReport.model_validate_json(
            response.output_text
        )

    def analyze_batch(
        self,
        pair1_reports: list[Pair1Report],
        pair2_reports: list[Pair2Report],
    ) -> list[AuditorReport]:

        reports = []

        for pair1, pair2 in zip(pair1_reports, pair2_reports):
            reports.append(
                self.analyze(
                    pair1,
                    pair2,
                )
            )

        return reports