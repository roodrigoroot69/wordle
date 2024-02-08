from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


DATABASE_URL = "postgresql://doadmin:AVNS_VwfCPQdLzfutDziTaU-@dd360-do-user-15693400-0.c.db.ondigitalocean.com:25060/defaultdb"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
