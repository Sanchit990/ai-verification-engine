# Transaction Schema

| Field | Type | Description |
|-------|------|-------------|
| Transaction_ID | String | Unique identifier assigned to the transaction |
| Customer_Name | String | Full name of the customer associated with the transaction |
| Customer_ID | String | Unique identifier assigned to the customer |
| Transaction_Date | Date | Date on which the transaction occurred or was recorded |
| Transaction_Amount | Float |Total monetary amount of the invoice|
| Transaction_Type | String | Indicates whether the transaction is a Credit or Debit |
| Currency | String |Three-letter currency code used for the transaction amount, such as INR or USD|
| Reference_Number | String | Payment, invoice, or other reference number associated with the transaction |
| Status | String | Current status of the transaction: Pending, Completed, Failed, Reversed|
| Description | String |Description or payment memo associated with the transaction |
| Payment_Mode | String |Actual payment method used for the transaction|
