from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar
import os
from dotenv import load_dotenv

load_dotenv()

#postgresql://myuser:password@localhost/
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

#Enable Query Cache
Select.inherit_cache = True
SelectOfScalar.inherit_cache = True

def create_session() -> Session:
    return Session(engine)
