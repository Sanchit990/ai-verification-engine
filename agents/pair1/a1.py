from pathlib import Path

from models.fullrecords import FullRecord
from models.agent_output import AgentOutput


class A1:

    def __init__(self):
        self.system_prompt = Path(
            "prompts/pair1/a1_system_prompt.md"
        ).read_text(encoding="utf-8")

    def build_prompt(self, fullrec: FullRecord) -> str:

        invoice = fullrec.invoice
        transaction = fullrec.transaction

        return f"""
Objective:
Determine whether the following invoice and transaction belong to the same payment.

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

==================================================
PRIMARY RULES
==================================================

1. Customer ID
2. Reference Number
3. Amount
4. Currency
5. Transaction Date should be within ±2 days of Invoice Date

==================================================
SECONDARY RULES
==================================================

1. Customer Name
2. Description
3. Payment Mode

==================================================
TASK
==================================================

Analyze the invoice and transaction.

1. Compare every primary rule.
2. Compare every secondary rule.
3. Record every match.
4. Record every violation.
5. Explain your reasoning.
6. Explain why confidence decreased if confidence is not 100%.
7. Return ONLY a JSON object matching the provided schema.
"""

    def analyze(self, fullrec: FullRecord) -> AgentOutput:

        prompt = self.build_prompt(fullrec)

        # Tomorrow:
        # 1. Send self.system_prompt + prompt to Gemini
        # 2. Parse JSON
        # 3. Validate using AgentOutput
        pass

    def analyze_batch(
        self,
        full_records: list[FullRecord]
    ) -> list[AgentOutput]:

        outputs = []

        for record in full_records:
            outputs.append(self.analyze(record))

        return outputs