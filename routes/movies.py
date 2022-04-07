from typing import List
from fastapi import APIRouter, Path, status, HTTPException
from movies import MoviesService

from movies import Movie, CreateMovie

movies_router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)

movies_user_router = APIRouter(
    prefix="/movies/user",
    tags=["movies-user"]
)

service = MoviesService()

@movies_router.get(
    '/',
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    summary="Show all movies",
    )
def get_movies():
    return service.get_all_movies()

@movies_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    summary="Create a new movie in the database",
    response_model=Movie
    )
def create_movie(movie: CreateMovie):
    return service.create_movie(movie)

@movies_router.get(
    '/{movie_id}',
    status_code=status.HTTP_200_OK,
    summary="Return a movie for the indicated id"
    )
def get_movie_by_id(movie_id: int = Path(
    ..., 
    title="Movie ID",
    description="This is the movie ID",
    example="5"
    )):
    """
    Show a Movie

    This path operation show a movie if the id exist in the database

    Parameters:
        - movie_id: int
    """
    movie = service.get_movie_by_id(movie_id)
    if(movie is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"¡This movie not exist!")
    return movie

@movies_router.put(
    '/{movie_id}',
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a movie with the provided data"
    )
def update_movie(movie: CreateMovie, movie_id: int = Path(...)):
    return service.update_movie(movie_id, movie)

@movies_router.delete(
    '/{movie_id}',
    status_code=status.HTTP_200_OK,
    summary="Delete the especified movie")
def delete_movie(movie_id: int = Path(...)):
    return service.delete_movie(movie_id)

@movies_user_router.get(
    '/',
)
def get_movies_user():
    return None

@movies_user_router.get(
    '/{movie_id}', 
)
def get_movie_user():
    return None

@movies_user_router.post(
    '/', 
)
def create_movie_user():
    return None

@movies_user_router.put(
    '/{movie_id}', 
)
def update_movie_user(movie_id: int = Path(...) ):
    return None

@movies_user_router.delete(
    '/{movie_id}', 
)
def update_movie_user(movie_id: int = Path(...) ):
    return None