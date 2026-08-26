from pydantic import BaseModel
from models.invoice import Invoice
from models.transaction import Transaction

class GroundTruth(BaseModel):
    invoice:Invoice
    transaction:Transaction
    expected_match:bool
    expected_reason:str
    error_type:str|None=None
