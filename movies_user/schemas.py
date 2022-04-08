from typing import Optional
from sqlmodel import Field, SQLModel

class BaseMovie(SQLModel):
    __tablename__ = "movies"

    title: str
    original_title: str
    romanised_title: str
    release_year: int = Field(gt=1900)
    wiki_link: str
    music: str
    duration: int = Field(gt=0)
    cover: str

class Movie(BaseMovie, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    @classmethod
    def from_dict(cls, values: dict): 
        return cls(
        id = values['id'] if 'id' in values else None,
        title= values['title'],
        original_title= values['original_title'],
        romanised_title= values['romanised_title'],
        release_year= values['release_year'],
        wiki_link= values['wiki_link'],
        music= values['music'],
        duration= values['duration'],
        cover= values['cover'])

class CreateMovie(BaseMovie):
    pass