from sqlmodel import select
from .schemas import CreateMovie, Movie
from database import create_session

class MoviesService:

    def get_all_movies(self):
        movies = []
        with create_session() as session:
            rows = session.execute(select(Movie)).scalars().all()
            movies = rows
            print(movies)
        return movies

    def get_movie_by_id(self, movie_id: int):
        with create_session as session:
            row = session.exec(select(Movie).where(Movie.id == movie_id)).first()
        
        return row

    def create_movie(self, movie: CreateMovie):
        movie = Movie.from_dict(movie.dict())
        with create_session as session:
            session.add(movie)
            session.flush()
            session.commit()
            session.refresh(movie)
            session.expunge(movie)
        return movie 

    def update_movie(self, movie_id, movie: CreateMovie):
        with create_session as session:
            session.merge(Movie.from_dict({**{"id": movie_id}, **movie.dict()}))
            session.flush()
            session.commit()
        return self.get_movie_by_id(movie_id)

    def delete_movie(self, movie_id):
        movie_bd = self.get_movie_by_id(movie_id)
        if movie_bd is None:
            return None
        
        with create_session as session:
            session.delete(movie_bd)
            session.commit()
        
        return movie_bd