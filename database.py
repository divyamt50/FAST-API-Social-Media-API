import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
database_password = os.environ.get("DATABASE_PASSWORD")

if not database_password:
    raise Exception("The environment variable DATABASE_PASSWORD must be set.")


SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{database_password}@localhost/FastAPI"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()