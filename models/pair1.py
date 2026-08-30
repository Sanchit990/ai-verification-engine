from pydantic import BaseModel
from models.agent_output import AgentOutput
from models.pair_consensus_report import PairConsensusReport
class Pair1Report(BaseModel):
    a1_output:AgentOutput
    a2_output:AgentOutput
    consensus_output:PairConsensusReport