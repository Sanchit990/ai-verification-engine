# Invoice Schema

| Field | Type | Description |
|-------|------|-------------|
| Invoice_ID | String | Unique identifier assigned to the invoice |
| Customer_ID | String | Unique identifier assigned to the customer |
| Reference_Number | String | Payment, invoice, or other reference number associated with the transaction |
| Customer_Name | String | Full name of the customer associated with the invoice |
| Invoice_Date | Date | Date on which the invoice was created or issued|
| Subtotal | Float |Total monetary amount of the invoice, excluding tax as specified|
| GST | Float |Goods and Services Tax amount charged on the invoice |
| Grand_Total | Float |Total monetary amount of the invoice|
| Currency | String |Three-letter currency code used for the invoice amount, such as INR or USD|
| Status | String | Current status of the transaction: Generated, Pending, Cancelled, Reconciled|
| Description | String |Description of the product(s) or service(s) purchased on the invoice |
| Payment_Mode | String |Expected payment method (UPI, NEFT, RTGS, Card, Cash, Cheque, etc.) |