from typing import List
from fastapi import APIRouter, Path, status, HTTPException
from movies_user import MoviesUserService
from movies_user.schemas import MovieUser, MovieUserResponse, CreateMovieUser, UpdateMovieUser

router = APIRouter(
    prefix="/movies/user",
    tags=["movies-user"]
)

service = MoviesUserService()

@router.get(
    '/',
    response_model=List[MovieUserResponse]
)
def get_movies_user():
    return service.get_all_movies_user(1)

@router.get(
    '/{movie_id}', 
    response_model=MovieUserResponse
)
def get_movie_user(movie_id: int = Path(...)):
    return service.get_movie_user_by_id(movie_id=movie_id, user_id=1)

@router.post(
    '/', 
)
def create_movie_user(movie_user: CreateMovieUser):
    return service.create_movie_user(movie_user)

@router.put(
    '/{movie_id}',
    response_model=MovieUser,
    response_model_exclude=['id']
)
def update_movie_user(movie_user: UpdateMovieUser, movie_id: int = Path(...)):
    return service.update_movie_user(movie_id=movie_id, movie_user=movie_user)

@router.delete(
    '/{movie_id}', 
)
def delete_movie_user(movie_id: int = Path(...) ):
    return service.delete_movie_user(movie_id=movie_id)