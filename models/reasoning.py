from pydantic import BaseModel

class Reasoning(BaseModel):
    observations: list[str]
    analysis_reasoning: list[str]
    conclusion: str