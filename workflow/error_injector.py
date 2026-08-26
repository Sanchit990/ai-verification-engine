import copy
import random

from models.invoice import Invoice
from models.transaction import Transaction


class ErrorInjector:

    def inject_amount_mismatch(
        self,
        transactions: list[Transaction],
        index: int
    ) -> dict:

        transaction = transactions[index]

        old_amount = transaction.transaction_amount

        transaction.transaction_amount = round(
            old_amount + random.uniform(100, 1000),
            2
        )

        return {
            "error_type": "AMOUNT_MISMATCH",
            "transaction_id": transaction.transaction_id,
            "old_value": old_amount,
            "new_value": transaction.transaction_amount,
        }

    def inject_currency_mismatch(
        self,
        transactions: list[Transaction],
        index: int
    ) -> dict:

        transaction = transactions[index]

        old_currency = transaction.currency

        available = ["USD", "EUR", "AED", "GBP"]

        available = [c for c in available if c != old_currency]

        transaction.currency = random.choice(available)

        return {
            "error_type": "CURRENCY_MISMATCH",
            "transaction_id": transaction.transaction_id,
            "old_value": old_currency,
            "new_value": transaction.currency,
        }

    def inject_missing_reference(
        self,
        transactions: list[Transaction],
        index: int
    ) -> dict:

        transaction = transactions[index]

        old_reference = transaction.reference_number

        transaction.reference_number = ""

        return {
            "error_type": "MISSING_REFERENCE",
            "transaction_id": transaction.transaction_id,
            "old_value": old_reference,
            "new_value": "",
        }

    def inject_duplicate_transaction(
        self,
        transactions: list[Transaction],
        index: int
    ) -> dict:

        duplicate = copy.deepcopy(transactions[index])

        duplicate.transaction_id = (
            duplicate.transaction_id + "_DUP"
        )

        transactions.append(duplicate)

        return {
            "error_type": "DUPLICATE_TRANSACTION",
            "original_transaction": transactions[index].transaction_id,
            "duplicate_transaction": duplicate.transaction_id,
        }

    def inject_missing_transaction(
        self,
        transactions: list[Transaction],
        index: int
    ) -> dict:

        removed = transactions.pop(index)

        return {
            "error_type": "MISSING_TRANSACTION",
            "transaction_id": removed.transaction_id,
        }

    def inject_errors(
        self,
        invoices: list[Invoice],
        transactions: list[Transaction]
    ) -> list[dict]:

        metadata = []

        total = len(transactions)

        used = set()

        def get_index():
            while True:
                i = random.randint(0, total - 1)
                if i not in used:
                    used.add(i)
                    return i

        metadata.append(
            self.inject_amount_mismatch(
                transactions,
                get_index()
            )
        )

        metadata.append(
            self.inject_currency_mismatch(
                transactions,
                get_index()
            )
        )

        metadata.append(
            self.inject_missing_reference(
                transactions,
                get_index()
            )
        )

        metadata.append(
            self.inject_duplicate_transaction(
                transactions,
                get_index()
            )
        )

        metadata.append(
            self.inject_missing_transaction(
                transactions,
                get_index()
            )
        )

        return metadata