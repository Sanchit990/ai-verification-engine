from faker import Faker 
import random
from models.invoice import Invoice
from models.transaction import Transaction
from models.ground_truth import GroundTruth
from datetime import timedelta
from typing import Tuple,List

class SyntheticDataGenerator:
   
    def __init__(self):
        self.fake=Faker()
        random.seed(42)
    
    def generate_invoice(self,index:int)->Invoice:
        total=round(random.uniform(1000,10001),2)
        gst_rate = random.choice([5, 12, 18, 28])
        gst_amount = round(total * gst_rate / 100, 2)
        grand_Total=round(total+gst_amount,2)
        payment_mode=["UPI","NEFT", "RTGS", "Card", "Cash","Cheque"]
        products = [ "Apple iPhone 16",
                    "Apple MacBook Air",
                    "Samsung Galaxy S25",
                    "Samsung Galaxy Tab"]

        return Invoice(
         invoice_id=f"INV-{index:04d}",
         customer_id=f"CUS-{index:04d}",
         customer_name=self.fake.name(), 
         reference_number=f"REF-{index:04d}",
         grand_total=grand_Total,
         subtotal=total,
         gst=gst_amount,
         invoice_date=self.fake.date_object(),
         currency="INR",
         status="Generated",
         description=random.choice(products),
         payment_mode=random.choice(payment_mode)
        )

    def generate_transaction(self,invoice:Invoice,index:int)->Transaction:

        return Transaction(
            transaction_id=f"TXN-{index:04d}",
            customer_id=invoice.customer_id,
            customer_name=invoice.customer_name,
            reference_number=invoice.reference_number,
            transaction_date= invoice.invoice_date+timedelta(days=random.randint(-2,2)),
            transaction_amount=invoice.grand_total,
            currency=invoice.currency,
            status="Completed",
            description=invoice.description,
            payment_mode=invoice.payment_mode,
            transaction_type="credit"

        )
    
    def generate_ground_truth(self,invoice:Invoice,transaction:Transaction)->GroundTruth:

        return GroundTruth(
            invoice=invoice,
            transaction=transaction,
            expected_match=True,
            expected_reason="All Matched",
            error_type=None
        )


    def generate_batch(self,count:int)->Tuple[List[Invoice], List[Transaction], List[GroundTruth]]:
        invoices=[]
        transactions=[]
        ground_truths=[]

        for i in range (1,count+1):
            invoice=self.generate_invoice(i)
            transaction=self.generate_transaction(invoice,i)
            truth=self.generate_ground_truth(invoice,transaction)
            transactions.append(transaction)
            invoices.append(invoice)
            ground_truths.append(truth)

        return invoices,transactions,ground_truths
    