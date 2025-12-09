# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from crud import create_survey_response, get_all_responses
from schemas import SurveyResponseCreate, SurveyResponseRead
from typing import List

# Create tables if they don’t exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Survey API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST endpoint to submit a survey response
@app.post("/survey", response_model=SurveyResponseRead)
def submit_survey(survey: SurveyResponseCreate, db: Session = Depends(get_db)):
    return create_survey_response(db, survey)

# GET endpoint to list all survey responses
@app.get("/survey", response_model=List[SurveyResponseRead])
def list_surveys(db: Session = Depends(get_db)):
    return get_all_responses(db)
