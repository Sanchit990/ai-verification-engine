from pydantic import BaseModel, Field

from models.reasoning import Reasoning
class JudgeReport(BaseModel):

    invoice_id: str

    transaction_id: str

    final_decision: str = Field(description="Allowed values: MATCH, NO_MATCH, UNCERTAIN")
    
    judge_reasoning: Reasoning

    final_confidence: float = Field( ge=0,le=1)

    next_action: str = Field(description="Allowed values: ACCEPT, RETRY, HUMAN_REVIEW")