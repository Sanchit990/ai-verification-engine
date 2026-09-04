from pydantic import BaseModel
from models.auditor_report import AuditorReport
from models.pair1 import Pair1Report
from models.pair2 import Pair2Report

class VerificationCase(BaseModel):
    pair1_report:Pair1Report
    pair2_report:Pair2Report
    auditor_report:AuditorReport 
