from sqlmodel import Session, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

#postgresql://myuser:password@localhost/
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

def create_session() -> Session:
    return Session(engine)

#SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)