from sqlalchemy import create_engine
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os
from dotenv import load_dotenv

load_dotenv()

#postgresql://myuser:password@localhost/
DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()