from typing import List
from fastapi import APIRouter, Path, status, HTTPException
from movies import MoviesService

from movies import Movie, CreateMovie

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)
service = MoviesService()

@router.get(
    '/',
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    summary="Show all movies",
    )
def get_movies():
    """
    This path operation return a list of all studio ghibli movies
    
    **Returns:** list (json array) of all studio ghibli movies

        - List[Movie] -> a list of Movie schema 
    """   
    return service.get_all_movies()

@router.get(
    '/{movie_id}',
    response_model=Movie,
    status_code=status.HTTP_200_OK,
    summary="Show the movie info for the especified movie id"
    )
def get_movie_by_id(
    movie_id: int = Path(
        ..., 
        title="Movie ID",
        description="Movie ID to get info",
        example="5"
        )
    ):
    """
    This path operation return movie info for the provided movie id

    **Parameters:**

        - Path paramters
            - movie_id: int
    
    **Returns:** movie info

        - movie: Movie
    """
    movie = service.get_movie_by_id(movie_id)
    if(movie is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"¡This movie not exist!")
    return movie
