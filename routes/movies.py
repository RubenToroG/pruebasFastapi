from typing import List
from fastapi import APIRouter, Path, status, HTTPException
from common.common_exceptions import HTTP_RESPONSE_404, HTTP_RESPONSE_500
from movies import MoviesService
from common import internal_server_error, not_found, HTTP_RESPONSE_404, HTTP_RESPONSE_500
from sqlalchemy.orm.exc import NoResultFound
from movies.schemas import Movie


router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)
service = MoviesService()

@router.get(
    '/',
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    responses={**HTTP_RESPONSE_500},
    summary="Show all movies",
    )
def get_movies():
    """
    This path operation return a list of all studio ghibli movies
    
    **Returns:** list (json array) of all studio ghibli movies

        - List[Movie] -> a list of Movie schema 
    """
    try:
        return service.get_all_movies()
    except:
        internal_server_error()

@router.get(
    '/{movie_id}',
    response_model=Movie,
    status_code=status.HTTP_200_OK,
    responses={**HTTP_RESPONSE_404, **HTTP_RESPONSE_500},
    summary="Show the movie info for the especified movie id"
    )
def get_movie_by_id(
    movie_id: int = Path(
        ..., 
        title="Movie ID",
        description="Movie ID to get info",
        example="5",
        ge=1
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
    try:
        movie = service.get_movie_by_id(movie_id)
        if(movie is None):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"¡This movie not exist!")
        return movie
    except NoResultFound:
        not_found(detail=f"Movie with id {movie_id} not found")
    except:
        internal_server_error()
