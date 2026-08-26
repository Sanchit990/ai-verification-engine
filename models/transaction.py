from datetime import date
from pydantic import BaseModel,Field

class Transaction(BaseModel):
    transaction_id:str=Field(description="Unique identifier assigned to the transaction")

    customer_id:str=Field(description="Unique identifier assigned to the customer")

    customer_name:str=Field(description="Full name of the customer associated with the transaction")

    transaction_date:date=Field(description="Date on which the transaction occurred or was recorded")

    transaction_amount:float=Field(ge=0,description="Total monetary amount of the invoice")

    transaction_type:str=Field(description="Indicates whether the transaction is a Credit or Debit")

    reference_number:str=Field(description="Payment, invoice, or other reference number associated with the transaction")

    currency:str=Field(description="Three-letter currency code used for the invoice amount, such as INR or USD")

    status:str=Field(description="Current status of the transaction: Pending, Completed, Failed, Reversed")

    description:str=Field(description="Description or payment memo associated with the transaction ")
    
    payment_mode:str=Field(description="Actual payment method used for the transaction")