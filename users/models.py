import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy.orm import declarative_base

import database as _database
Base = declarative_base()

class User(Base):
    __tablename__ = "user_info"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, index=True, unique=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    nick_name = _sql.Column(_sql.String, index=True, unique=True)
    profile_picture = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)