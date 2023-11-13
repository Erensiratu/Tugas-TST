from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

DATABASE_PASSWORD = "Chels!A4"
ENCODED_PASSWORD = quote_plus(DATABASE_PASSWORD)

DATABASE_URL = f"postgresql://erensiratu:{ENCODED_PASSWORD}@recycodatabase.postgres.database.azure.com:5432/recycodatabase?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()