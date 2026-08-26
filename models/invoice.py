from pydantic import BaseModel,Field
from datetime import date

class Invoice(BaseModel):
    invoice_id:str=Field(description="Unique identifier assigned to the invoice ")

    customer_id:str=Field(description="Unique identifier assigned to the customer ")

    reference_number:str=Field(description="Payment, invoice, or other reference number associated with the transaction")

    customer_name:str=Field(description="Full name of the customer associated with the invoice")

    invoice_date:date=Field(description="Date on which the invoice was created or issued")

    subtotal:float=Field(ge=0,description="Total monetary amount of the invoice, excluding tax as specified")

    gst:float=Field(ge=0,description="Goods and Services Tax amount charged on the invoice")

    grand_total:float=Field(ge=0,description="Total monetary amount of the invoice")

    currency:str=Field(description="Three-letter currency code used for the invoice amount, such as INR or USD")

    status:str=Field(description="Current status of the transaction: Generated, Pending, Cancelled, Reconciled")

    description:str=Field(description="Description of the product(s) or service(s) purchased on the invoice")
    
    payment_mode:str=Field(description="Expected payment method (UPI, NEFT, RTGS, Card, Cash, Cheque, etc.)")