from data.synthetic_data_generator import SyntheticDataGenerator
from workflow.error_injector import ErrorInjector
from workflow.data_processor import DataPreprocessor

from agents.pair1 import A1, A2
from agents.pair1.consensus import ConsensusEngine

# Uncomment after Pair 2 is ready
# from agents.pair2 import Q5, Q6
# from agents.pair2.consensus import ConsensusEngine as Pair2Consensus

# Uncomment after Auditor is ready
# from agents.auditor.auditor import Auditor


def main():

    # STEP 1 : Generate Golden Dataset


    generator = SyntheticDataGenerator()

    invoices, transactions = generator.generate_batch(1)


    # STEP 2 : Create Working Copy


    working_invoices, working_transactions = (
        generator.create_working_copy(
            invoices,
            transactions,
        )
    )


    # STEP 3 : Inject Errors


    injector = ErrorInjector()

    metadata = injector.inject_errors(
        working_invoices,
        working_transactions,
    )


    # STEP 4 : Preprocess


    preprocessor = DataPreprocessor()

    full_records = preprocessor.create_full_records(
        working_invoices,
        working_transactions,
    )

    primary_records = preprocessor.create_primary_records(
        full_records,
    )


    # STEP 5 : Pair 1


    a1 = A1()
    a2 = A2()

    a1_outputs = a1.analyze_batch(full_records)
    a2_outputs = a2.analyze_batch(full_records)

    pair1_consensus = ConsensusEngine()

    pair1_reports = pair1_consensus.analyze_batch(
        a1_outputs,
        a2_outputs,
    )


    # STEP 6 : Pair 2


    # q5 = Q5()
    # q6 = Q6()

    # q5_outputs = q5.analyze_batch(primary_records)
    # q6_outputs = q6.analyze_batch(primary_records)

    # pair2_consensus = Pair2Consensus()

    # pair2_reports = pair2_consensus.analyze_batch(
    #     q5_outputs,
    #     q6_outputs,
    # )


    # STEP 7 : Auditor

    # auditor = Auditor()

    # auditor_reports = auditor.analyze_batch(
    #     pair1_reports,
    #     pair2_reports,
    # )


    # Debug

    print("=" * 60)
    print("PAIR 1 REPORT")
    print("=" * 60)

    for report in pair1_reports:
        print(report)
        print()


if __name__ == "__main__":
    main()





# invoice = Invoice(
#     invoice_id="INV001",
#     customer_id="C001",
#     reference_number="REF123",
#     customer_name="Alice",
#     invoice_date=date(2026, 8, 23),
#     subtotal=1000,
#     gst=180,
#     grand_total=1180,
#     currency="INR",
#     status="Generated",
#     description="MacBook Pro",
#     payment_mode="UPI"
# )

# print(invoice)

# transaction= Transaction(
#     transaction_id="TXN-10045",
#     customer_id="CUS-204",
#     customer_name="Sanchit Chauhan",
#     transaction_date=date(2026, 8, 23),
#     transaction_amount=15000.50,
#     transaction_type="Debit",
#     reference_number="INV-10045",
#     currency="INR",
#     status="Completed",
#     description="Payment for laptop purchase",
#     payment_mode="UPI"
# )


# print(transaction)



























# from pydantic import BaseModel,ConfigDict
# from typing import Optional
# from datetime import datetime

# class User(BaseModel):
#     id:int
#     name:str='james'
#     signup_time:Optional[datetime]=None


# m=User.model_validate({'id':'1234','name':'jhon'}) #can provide dictonary input 

# print(m)

# m=User.model_validate_json('{"id":1234, "name":"james"}')

# print(m)




























# class A(BaseModel):
#     count:int 
#     size:Optional[float]=None

# class B(BaseModel):
#     apple:str='x'
#     banana:str='y'


# class c(BaseModel):
#     a:A
#     b:list[B]
#     a1:A
#     b1:list[B]


# m = c(
#     a={'count': 10, 'size': 4},

#     b=[
#         {'apple': 'red', 'banana': 'yellow'},
#         {'apple': 'green', 'banana': 'green'},
#         {'apple': 'pink'},
#         {'banana': 'black'}
#     ],

#     a1={'count': '15', 'size': 4},

#     b1=[
#         {'apple': 'red', 'banana': 'yellow'},
#         {'apple': 'green', 'banana': 'green'},
#         {'apple': 'pink'},
#         {'banana': 'black'}
#     ]
# )

# print(m)


# print(m.model_dump())


























# user=User(name="Sanchit Chauhan" , id='1234')


# assert user.name=="Sanchit Chauhan"
# assert user.id==1234
# assert isinstance(user.id,int)
# assert isinstance(user.name, str)
# print(user) #expecting my name Sanchit Chauhan 


# assert user.model_dump()=={'id':1234 ,'name':'Sanchit Chauhan'}























# import base64
# from google import genai
# from dotenv import load_dotenv

# load_dotenv()
# client=genai.Client()

# interaction=client.interactions.create(
#     model="gemini-2.5-flash-image",
#     input="create me an image of super car"
# )
# with open("generated_image.png","wb") as f:
#     f.write(base64.b64decode(interaction.output_image.data))



















# with open("dog-on-isolated-background-png.png.webp","rb") as f:
#     image_byte=f.read()
#     image_b64=base64.b64encode(image_byte).decode("uft-8")

# interection=client.interactions.create(
# model="gemini-3.6-flash",
# input=[
#     {
#         "type":"text","text":"this is a image tell me what it is u think"},
#     {
#         "type":"image",
#         "data":image_b64,
#         "mime_type":"image/webp"
#     }
# ]
# )
# print(interection)
















# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# client = genai.Client()

# response= client.interactions.create(
#     model="gemini-3.6-flash",
#     input="hello i have a dog, it has 4 paws",
# )

# print(response.output_text)

# response2=client.interactions.create(
#     model='gemini-3.6-flash',
#     input='how many paws does it have',
#     previous_interaction_id=response.id,
# )
# print(response2.output_text)

