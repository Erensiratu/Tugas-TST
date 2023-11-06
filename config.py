from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_PASSWORD = "Chels!A4"
ENCODED_PASSWORD = quote_plus(DATABASE_PASSWORD)

DATABASE_URL = f"postgresql://erensiratu:{ENCODED_PASSWORD}@recycodb.postgres.database.azure.com:5432/recyco_db?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()