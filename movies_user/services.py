from sqlalchemy import and_
from sqlmodel import Session, select
from movies.schemas import MovieDB, Movie
from .schemas import CreateMovieUser, MovieUser, MovieUserResponse
from database import create_session

class MoviesUserService:

    def get_all_movies_user(self, user_id: int):
        movies = []
        with create_session() as session:
            query = (select(MovieUser.user_score, MovieDB)
                    .join(MovieDB, MovieDB.id == MovieUser.id_movie)
                    .where(MovieUser.id_user == user_id)
                    )
            rows = session.exec(query).all()
            movies = [MovieUserResponse(user_score=row[0], movie=Movie.from_moviedb(row[1])) for row in rows]
        return movies

    def get_movie_user_by_id(self, user_id, movie_id: int):
        with create_session() as session:
            query = (select(MovieUser.user_score, MovieDB)
                    .join(MovieDB, MovieDB.id == MovieUser.id_movie)
                    .where(MovieUser.id_user == user_id and MovieUser.id_movie == movie_id)
                    )   
            row = session.exec(query).one()
            movie = MovieUserResponse(user_score=row[0], movie=Movie.from_moviedb(row[1]))
        return movie

    def create_movie_user(self, movie_user: CreateMovieUser):
        new_movie_user = MovieUser.from_dict(movie_user.dict())
        with create_session() as session:
            session.add(new_movie_user)
            session.flush()
            session.commit()
            session.refresh(new_movie_user)
            session.expunge(new_movie_user)
        return new_movie_user   

    def update_movie_user(self, movie_id: int, movie_user: CreateMovieUser):
        with create_session() as session:
            movie_user_db = self.__get_movie_user_by_id(movie_id, session)
            movie_user_db.user_score = movie_user.user_score
            session.merge(movie_user_db)
            session.flush()
            session.commit()
            session.refresh(movie_user_db)
            session.expunge(movie_user_db)
        return movie_user_db

    def delete_movie_user(self, movie_id: int, user_id: int):
        with create_session() as session:
            query = (select(MovieUser)
                    .where(
                        and_(
                            MovieUser.id_movie == movie_id,
                            MovieUser.id_user == user_id
                        )
                    ))
            movie_bd = session.exec(query).one()
            
            session.delete(movie_bd)
            session.commit()
        return movie_bd
    
    def __get_movie_user_by_id(self, movie_user_id: int, session: Session) -> MovieUser:
        return session.exec(select(MovieUser).where(MovieUser.id == movie_user_id)).one()