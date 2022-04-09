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
    response_model=List[MovieUserResponse],
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
    summary="Show all viewed movies by the user",
)
def get_movies_user():
    """
    This path operation return a list of viewed movies for the user
  
    **Returns:** a list (json array) with the viewed movies:

        - List[MovieUserResponse] -> a list of MovieUserResponse schema without average_score
    """
    return service.get_all_movies_user(1)

@router.get(
    '/{movie_id}', 
    response_model=MovieUserResponse, 
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
    summary="Show information for specified viewed movie",
)
def get_movie_user(
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="This is the movie ID to obtain information",
        example="3"
        )
    ):
    """
    This path operation return the information of a espcific viewed movie
    
    **Parameters:**

        - Path parameters:
            - movie_id: int

    **Returns:** viewed movie information in json format:

        - MovieUserResponse schema without average_score
    """
    return service.get_movie_user_by_id(movie_id=movie_id, user_id=1)

@router.post(
    '/', 
    response_model=MovieUser,
    response_model_exclude=['id'],
    status_code=status.HTTP_201_CREATED,
    summary="Save a movie as viewed by the user",
)
def create_movie_user(movie_user: CreateMovieUser):
    """
    This path operation saves a movie as seen by the user
    
    **Parameters:**

        - Request body parameters:
            - movie_user: CreateMovieUser

    **Returns:** movie information added to viewed movies

        - MovieUser schema
    """
    return service.create_movie_user(movie_user)

@router.put(
    '/{movie_id}',
    response_model=MovieUser,
    response_model_exclude=['id'],
    status_code=status.HTTP_200_OK,
    summary="Update the user score for the viewed movie",
)
def update_movie_user(
    movie_user: UpdateMovieUser,
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="This is the movie ID to update the user_score",
        example="3"
        )
    ):
    """
    This path operation update the user score for the viewed movie
    
    **Parameters:**

        -Path parameters:
            - movie_id: int 

        - Request body parameters:
            - movie_user: UpdateMovieUser

    **Returns:** updated movie information

        - MovieUser schema
    """
    return service.update_movie_user(movie_id=movie_id, movie_user=movie_user)

@router.delete(
    '/{movie_id}', 
    response_model=MovieUser,
    response_model_exclude=['id'],
    status_code=status.HTTP_200_OK,
    summary="Delete a movie from the viewed movies",
)
def delete_movie_user(
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="This is the movie ID to delete from viewed list",
        example="3"
        )
    ):
    """
    This path operation delete the movie from the viewed movies by the user
    
    **Parameters:**

        -Path parameters:
            - movie_id: int 

    **Returns:** deleted movie information

        - MovieUser schema
    """
    return service.delete_movie_user(movie_id=movie_id, user_id=1)