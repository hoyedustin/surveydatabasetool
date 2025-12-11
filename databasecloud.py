# databasecloud.py
from google.cloud.sql.connector import Connector, IPTypes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Optional: load .env only for local development
from dotenv import load_dotenv
load_dotenv()

# Cloud SQL connection info
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")  # e.g. "project:region:instance"
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# Initialize the Cloud SQL Connector
connector = Connector()

def getconn():
    """Return a database connection for SQLAlchemy"""
    return connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME,
        ip_type=IPTypes.PUBLIC  # Use PRIVATE if you have VPC configured
    )

# Create the SQLAlchemy engine using the connector
engine = create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# SQLAlchemy session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
