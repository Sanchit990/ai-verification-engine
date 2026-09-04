from pydantic import BaseModel
from models.agent_output import AgentOutput
from models.pair_consensus_report import PairConsensusReport
class Pair2Report(BaseModel):
    pair2_a1:AgentOutput
    pair2_a2:AgentOutput
    pair2_consensus:PairConsensusReport