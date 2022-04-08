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

@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    summary="Create a new movie in the database",
    response_model=Movie
    )
def create_movie(movie: CreateMovie):
    """
    This path operation create a new studio ghibli movie
    
    **Parameters:**

        - Request body parameters:
            - movie: CreateMovie

    **Returns:** added movie info
    
        - Movie schema
    """  
    return service.create_movie(movie)

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

@router.put(
    '/{movie_id}',
    response_model=Movie,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a movie with the provided data"
    )
def update_movie(
    movie: CreateMovie,
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="Movie ID to update info",
        example="5"
        )
    ):
    """
    This path operation update the movie info for the especified id

    **Parameters:**

        - Path paramters
            - movie_id: int
        
        -Request body parameters:
            - movie: CreateMovie
    
    **Returns:** updated movie info

        - Movie schema
    """
    return service.update_movie(movie_id, movie)

@router.delete(
    '/{movie_id}',
    response_model=Movie,
    status_code=status.HTTP_200_OK,
    summary="Delete the especified movie")
def delete_movie(
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="Movie ID to delete",
        example="5"
        )
    ):
    """
    This path operation delete a movie

    **Parameters:**

        - Path paramters
            - movie_id: int
           
    **Returns:** deleted movie info

        - Movie schema
    """
    return service.delete_movie(movie_id)