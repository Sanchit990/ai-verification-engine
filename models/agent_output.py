from pydantic import BaseModel,Field
from models.reasoning import Reasoning

class AgentOutput(BaseModel):
    invoice_id:str=Field(description="Unique invoice identifier")
    transaction_id:str=Field(description="Unique transaction identifier")
    match_decision:str=Field(description="Final reconciliation decision. Allowed values: MATCH, NO_MATCH, UNCERTAIN")
    confidence:float=Field(description="Confidence level of verification")
    confidence_drop_reason:list[str]=Field(ge=0,le=100,description="Reason to dropoff confidence")
    evidence:list[str]=Field(description="Factual data")
    violations:list[str]=Field(description="Rules violated")
    reasoning:Reasoning=Field(description="Explanation of how the agent reached its final decision")
    warnings:list[str]=Field(description="Warnings encountered during analysis that may reduce confidence but do not necessarily indicate a mismatch")
    