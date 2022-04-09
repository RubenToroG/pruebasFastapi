from typing import Optional
from sqlmodel import Field, SQLModel, ForeignKey, Column, Integer

from movies.schemas import Movie

class BaseMovieUser(SQLModel):
    __tablename__ = "view_movie"

    id_movie: int = Field(
        sa_column=Column(Integer, ForeignKey('movie.id'))
        )
    id_user: int = Field(
        sa_column=Column(Integer, ForeignKey('user.id'))
        )
    user_score: Optional[float]


class MovieUser(BaseMovieUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    @classmethod
    def from_dict(cls, values: dict):
        return cls(
            id = values['id'] if 'id' in values else None,
            id_movie = values['id_movie'],
            id_user = values['id_user'],
            user_score = values['user_score']
        )

class CreateMovieUser(BaseMovieUser):
    pass

class UpdateMovieUser(SQLModel):
    user_score: float = Field(gt=0, lt=5)

class MovieUserResponse(SQLModel):
    user_score: Optional[float]
    movie: Movie

