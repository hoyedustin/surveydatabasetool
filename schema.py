# schemas.py
from pydantic import BaseModel

# Schema for incoming survey responses (POST)
class SurveyResponseCreate(BaseModel):
    name: str
    email: str
    feedback: str

# Schema for outgoing survey responses (GET)
class SurveyResponseRead(BaseModel):
    id: int
    name: str
    email: str
    feedback: str

    class Config:
        orm_mode = True
