from pathlib import Path

from config.gemini_client import client
from models.primaryrecords import PrimaryRecord
from models.agent_output import AgentOutput


class A1:

    def __init__(self):

        self.client = client

        self.system_prompt = Path("prompts/pair2/a1_system_prompt.md").read_text(encoding="utf-8")

    def build_prompt(self,record: PrimaryRecord) -> str:

        return f"""
==================================================
INVOICE
==================================================

Invoice ID: {record.invoice_id}
Customer ID: {record.invoice_customer_id}
Reference Number: {record.invoice_reference_number}
Invoice Date: {record.invoice_date}
Grand Total: {record.invoice_grand_total}
Currency: {record.invoice_currency}

==================================================
TRANSACTION
==================================================

Transaction ID: {record.transaction_id}
Customer ID: {record.transaction_customer_id}
Reference Number: {record.transaction_reference_number}
Transaction Date: {record.transaction_date}
Transaction Amount: {record.transaction_amount}
Transaction Type: {record.transaction_type}
Currency: {record.transaction_currency}
"""

    def analyze(self, record: PrimaryRecord) -> AgentOutput:

        prompt = self.build_prompt(record)

        response = self.client.interactions.create(

            model="gemini-3.6-flash",

            input=f"{self.system_prompt}\n\n{prompt}",

            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": AgentOutput.model_json_schema(),
            },
        )

        return AgentOutput.model_validate_json(
            response.output_text
        )

    def analyze_batch(self,records: list[PrimaryRecord]) -> list[AgentOutput]:

        outputs: list[AgentOutput] = []

        for record in records:
            outputs.append(
                self.analyze(record)
            )

        return outputs