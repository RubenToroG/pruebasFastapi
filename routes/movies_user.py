from typing import List
from fastapi import APIRouter, Path, status, HTTPException
from movies import MoviesService

from movies import Movie, CreateMovie

router = APIRouter(
    prefix="/movies/user",
    tags=["movies-user"]
)

service = MoviesService()

@router.get(
    '/',
)
def get_movies_user():
    return None

@router.get(
    '/{movie_id}', 
)
def get_movie_user():
    return None

@router.post(
    '/', 
)
def create_movie_user():
    return None

@router.put(
    '/{movie_id}', 
)
def update_movie_user(movie_id: int = Path(...) ):
    return None

@router.delete(
    '/{movie_id}', 
)
def update_movie_user(movie_id: int = Path(...) ):
    return None