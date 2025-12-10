# database.py
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base

connector = Connector()

def getconn():
    conn = connector.connect(
        "YOUR_PROJECT:YOUR_REGION:YOUR_INSTANCE_NAME",
        "pymysql",
        user="YOUR_DB_USER",
        password="YOUR_DB_PASSWORD",
        db="survey_database",
        ip_type=IPTypes.PUBLIC  # or IPTypes.PRIVATE if using VPC
    )
    return conn

# Create SQLAlchemy engine
engine = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
