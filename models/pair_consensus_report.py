from pydantic import BaseModel
from models.agent_output import AgentOutput
from models.reasoning import Reasoning

class PairConsensusReport(BaseModel):
    invoice_id: str

    transaction_id: str

    agent1_output: AgentOutput

    agent2_output: AgentOutput

    final_decision: str

    final_confidence: float

    consensus_evidence: list[str]

    disagreements: list[str]

    consensus_reasoning: Reasoning

    next_action: str