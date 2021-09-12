from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


USER_DB = os.environ.get("POSTGRES_USER")
PASS_DB = os.environ.get("POSTGRES_PASSWORD")
SERVER_DB = os.environ.get("POSTGRES_HOST")
NAME_DB = os.environ.get("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@0.0.0.0/postgres"


# SQLALCHEMY_DATABASE_URL = f"postgresql://{USER_DB}:{PASS_DB}@postgres:5432/{NAME_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
