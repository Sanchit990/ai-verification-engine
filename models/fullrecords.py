from pydantic import BaseModel
from models.invoice import Invoice
from models.transaction import Transaction

class FullRecord(BaseModel):
    invoice:Invoice
    transaction:Transaction