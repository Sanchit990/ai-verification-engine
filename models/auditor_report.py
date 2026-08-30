from pydantic import BaseModel, Field

from models.reasoning import Reasoning
from models.pair1 import Pair1Report
from models.pair2 import Pair2Report   


class AuditorReport(BaseModel):

    invoice_id: str

    transaction_id: str

    pair1_report: Pair1Report

    pair2_report: Pair2Report

    recommended_pair: str

    audit_findings: list[str]

    audit_reasoning: Reasoning

    final_confidence: float = Field(ge=0,le=1,)

    next_action: str 