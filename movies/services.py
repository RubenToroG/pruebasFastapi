from sqlmodel import select, func, and_
from .schemas import CreateMovie, Movie, MovieDB
from database import create_session
from movies_user.schemas import MovieUser
class MoviesService:

    def get_all_movies(self):
        movies = []
        with create_session() as session:
            query = (
                    select(func.avg(MovieUser.user_score).label('user_score'), MovieDB)
                    .where(
                        and_(
                            MovieUser.id_movie == MovieDB.id,
                            MovieUser.user_score != None
                        )
                    )
                    .group_by(MovieDB.id)
                    )
            rows = session.exec(query).all()
            movies = [Movie.from_moviedb(movie[1], movie[0]) for movie in rows]
        return movies

    def get_movie_by_id(self, movie_id: int):
        with create_session() as session:
            query = (
                select(func.avg(MovieUser.user_score).label('user_score'), MovieDB)
                .where(
                    and_(
                        MovieUser.id_movie == MovieDB.id,
                        MovieUser.user_score != None,
                        MovieDB.id == movie_id
                    )
                )
                .group_by(MovieDB.id)
                )
            row = session.exec(query).one()
            movie = Movie.from_moviedb(row[1], row[0])
        return movie