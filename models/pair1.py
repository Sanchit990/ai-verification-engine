from pydantic import BaseModel
from models.agent_output import AgentOutput
from models.pair_consensus_report import PairConsensusReport
class Pair1Report(BaseModel):
    pair1_a1:AgentOutput
    pair1_a2:AgentOutput
    pair1_consensus:PairConsensusReport