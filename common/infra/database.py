from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


DATABASE_URL = "postgresql://jgtiztew:34lBlhTD5ups6oT1MBWFjYKWCQDPjEsk@baasu.db.elephantsql.com/jgtiztew"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
