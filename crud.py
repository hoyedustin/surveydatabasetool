# crud.py
from sqlalchemy.orm import Session
from models import SurveyResponse
from schemas import SurveyResponseCreate

def create_survey_response(db: Session, survey: SurveyResponseCreate):
    db_survey = SurveyResponse(
        name=survey.name,
        email=survey.email,
        feedback=survey.feedback  # <-- fixed field name
    )
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def get_all_responses(db: Session):
    return db.query(SurveyResponse).all()
