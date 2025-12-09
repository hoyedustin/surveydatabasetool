# schemas.py
from pydantic import BaseModel

# Schema for incoming survey responses (POST)
class SurveyResponseCreate(BaseModel):
    name: str
    email: str
    feedback: str

# Schema for outgoing survey responses (GET)
class SurveyResponseRead(BaseModel):
    name: str
    email: str
    response: str

    class Config:
        orm_mode = True
