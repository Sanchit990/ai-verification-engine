from pydantic import BaseModel, Field

from models.reasoning import Reasoning
from models.pair1 import Pair1Report
from models.pair2 import Pair2Report
from models.auditor_report import AuditorReport


class JudgeReport(BaseModel):

    invoice_id: str

    transaction_id: str

    pair1_report: Pair1Report

    pair2_report: Pair2Report

    auditor_report: AuditorReport

    final_decision: str = Field(
        description="Allowed values: MATCH, NO_MATCH, UNCERTAIN"
    )

    judge_reasoning: Reasoning

    final_confidence: float = Field(
        ge=0,
        le=1
    )

    next_action: str = Field(
        description="Allowed values: ACCEPT, RETRY, HUMAN_REVIEW"
    )