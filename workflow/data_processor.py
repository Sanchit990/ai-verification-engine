from models.invoice import Invoice
from models.transaction import Transaction
from models.fullrecords import FullRecord
from models.primaryrecords import PrimaryRecord


class DataPreprocessor:

    def create_full_records(
        self,
        invoices: list[Invoice],
        transactions: list[Transaction]
    ) -> list[FullRecord]:

        full_records = []

        for invoice, transaction in zip(invoices, transactions):

            full_records.append(
                FullRecord(
                    invoice=invoice,
                    transaction=transaction
                )
            )

        return full_records

    def create_primary_records(
        self,
        full_records: list[FullRecord]
    ) -> list[PrimaryRecord]:

        primary_records = []

        for record in full_records:

            primary_records.append(

                PrimaryRecord(

                    invoice_id=record.invoice.invoice_id,
                    transaction_id=record.transaction.transaction_id,

                    invoice_customer_id=record.invoice.customer_id,
                    transaction_customer_id=record.transaction.customer_id,

                    invoice_reference_number=record.invoice.reference_number,
                    transaction_reference_number=record.transaction.reference_number,

                    invoice_date=record.invoice.invoice_date,
                    transaction_date=record.transaction.transaction_date,

                    invoice_grand_total=record.invoice.grand_total,
                    transaction_amount=record.transaction.transaction_amount,

                    invoice_currency=record.invoice.currency,
                    transaction_currency=record.transaction.currency,

                    transaction_type=record.transaction.transaction_type

                )

            )

        return primary_records