#TODO:
# Convert confidence from 0-1 to percentage (0-100)
from pathlib import Path
from config.gemini_client import client
from models.fullrecords import FullRecord
from models.agent_output import AgentOutput


class A1:

    def __init__(self):
        self.client = client

        self.system_prompt = Path("prompts/pair1/a1_system_prompt.md").read_text(encoding="utf-8")

    def build_prompt(self,fullrec:FullRecord)->str:

        invoice = fullrec.invoice
        transaction = fullrec.transaction

        return f"""
==================================================
INVOICE
==================================================

Invoice ID: {invoice.invoice_id}
Customer ID: {invoice.customer_id}
Customer Name: {invoice.customer_name}
Reference Number: {invoice.reference_number}
Invoice Date: {invoice.invoice_date}
Subtotal: {invoice.subtotal}
GST: {invoice.gst}
Grand Total: {invoice.grand_total}
Currency: {invoice.currency}
Status: {invoice.status}
Description: {invoice.description}
Payment Mode: {invoice.payment_mode}

==================================================
TRANSACTION
==================================================

Transaction ID: {transaction.transaction_id}
Customer ID: {transaction.customer_id}
Customer Name: {transaction.customer_name}
Reference Number: {transaction.reference_number}
Transaction Date: {transaction.transaction_date}
Transaction Amount: {transaction.transaction_amount}
Transaction Type: {transaction.transaction_type}
Currency: {transaction.currency}
Status: {transaction.status}
Description: {transaction.description}
Payment Mode: {transaction.payment_mode}
"""

    def analyze(self,fullrec:FullRecord)->AgentOutput:

        prompt = self.build_prompt(fullrec)
        response = self.client.interactions.create(
            model="gemini-3.6-flash",
            input=f"{self.system_prompt}\n\n{prompt}",
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": AgentOutput.model_json_schema()
            },
        )

        return AgentOutput.model_validate_json(response.output_text)

    def analyze_batch(self,full_records:list[FullRecord])->list[AgentOutput]:

        outputs: list[AgentOutput]=[]

        for record in full_records:
            outputs.append(self.analyze(record))

        return outputs