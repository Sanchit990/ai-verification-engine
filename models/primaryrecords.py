from datetime import date
from pydantic import BaseModel

class PrimaryRecord(BaseModel):

    invoice_id: str
    transaction_id: str

    invoice_customer_id: str
    transaction_customer_id: str

    invoice_reference_number: str
    transaction_reference_number: str

    invoice_date: date
    transaction_date: date

    invoice_grand_total: float
    transaction_amount: float

    invoice_currency: str
    transaction_currency: str

    transaction_type: str