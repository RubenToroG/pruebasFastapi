import datetime as _dt
from unicodedata import name
import sqlalchemy as _sql
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Movies(Base):
    __tablename__ = "movies"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True, unique=True)
    original_title = _sql.Column(_sql.String, index=True, unique=True)
    romanised_title = _sql.Column(_sql.String, index=True, unique=True)
    release_year = _sql.Column(_sql.Integer)
    wiki_link = _sql.Column(_sql.Text)
    music = _sql.Column(_sql.String)
    duration = _sql.Column(_sql.Integer)
    cover = _sql.Column(_sql.Text)