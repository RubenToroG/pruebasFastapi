from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship

class MoviesProducers(SQLModel, table=True):
    __tablename__ = 'movies_producers'

    id_movie: int = Field(foreign_key='movies.id', primary_key=True)
    id_producer: int = Field(foreign_key='producers.id', primary_key=True)

class MoviesScreenwriters(SQLModel, table=True):
    __tablename__ = 'movies_screenwriters'
    
    id_movie: int = Field(foreign_key='movies.id', primary_key=True)
    id_screenwriter: int = Field(foreign_key='screenwriters.id', primary_key=True)

class Producer(SQLModel, table=True):
    __tablename__ = 'producers'

    id: int = Field(primary_key=True, default=None)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)

    movies: List["MovieDB"] = Relationship(back_populates='producers', link_model=MoviesProducers)

class Screenwriter(SQLModel, table=True):
    __tablename__ = 'screenwriters'

    id: int = Field(primary_key=True, default=None)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)

    movies: List["MovieDB"] = Relationship(back_populates='screenwriters', link_model=MoviesScreenwriters)
class BaseMovie(SQLModel):
    __tablename__ = "movies"

    title: str
    original_title: str
    romanised_title: str
    release_year: int = Field(gt=1900)
    wiki_link: Optional[str]
    music: str
    duration: int = Field(gt=0)
    cover: Optional[str]
    banner:Optional[str]

class MovieDB(BaseMovie, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    producers: List[Producer] =  Relationship(back_populates="movies", link_model=MoviesProducers)
    screenwriters: List[Screenwriter] = Relationship(back_populates="movies", link_model=MoviesScreenwriters)

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
        cover= values['cover'],
        banner= values['banner'],
        )

class Movie(BaseMovie):
    id: int = Field(primary_key=True, default=None)
    producers: List[Producer] 
    screenwriters: List[Screenwriter] 
    average_score: Optional[float] = Field(default=None)
    
    @classmethod
    def from_moviedb(cls, movie: MovieDB, average_score: float = None):
        return cls(
            id = movie.id,
            title = movie.title,
            original_title = movie.original_title, 
            romanised_title = movie.romanised_title, 
            release_year = movie.release_year,
            wiki_link = movie.wiki_link,
            music = movie.music,
            duration = movie.duration,
            cover = movie.cover,
            producers = movie.producers,
            screenwriters = movie.screenwriters,
            average_score = average_score,
            banner=movie.banner
        )

class CreateMovie(BaseMovie):
    pass