# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class SurveyResponse(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    response = Column(String(500), nullable=False)