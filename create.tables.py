# create_tables.py
from databasecloud import engine, Base
from models import SurveyResponse

# This will create all tables defined in your models if they don't exist yet
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
