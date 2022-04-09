from operator import ge
from typing import List
from fastapi import APIRouter, Path, status
from common.common_exceptions import HTTP_RESPONSE_404, HTTP_RESPONSE_500, internal_server_error, not_found
from movies_user import MoviesUserService
from movies_user.schemas import MovieUser, MovieUserResponse, CreateMovieUser, UpdateMovieUser
from sqlalchemy.orm.exc import NoResultFound

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
    responses={**HTTP_RESPONSE_404, **HTTP_RESPONSE_500},
    summary="Show information for specified viewed movie",
)
def get_movie_user(
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="This is the movie ID to obtain information",
        example="3",
        ge=1
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
    try:
        return service.get_movie_user_by_id(movie_id=movie_id, user_id=1)
    except NoResultFound:
        not_found(f"The user has not seen the movie with id {movie_id}")
    except:
        internal_server_error()

@router.post(
    '/', 
    response_model=MovieUser,
    response_model_exclude=['id'],
    status_code=status.HTTP_201_CREATED,
    responses={**HTTP_RESPONSE_500},
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
    try:
        return service.create_movie_user(movie_user)
    except:
        internal_server_error()

@router.put(
    '/{movie_id}',
    response_model=MovieUser,
    response_model_exclude=['id'],
    status_code=status.HTTP_200_OK,
    responses={**HTTP_RESPONSE_404, **HTTP_RESPONSE_500},
    summary="Update the user score for the viewed movie",
)
def update_movie_user(
    movie_user: UpdateMovieUser,
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="This is the movie ID to update the user_score",
        example="3",
        ge=1
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
    try:
        return service.update_movie_user(movie_id=movie_id, movie_user=movie_user)
    except NoResultFound:
        not_found(f"The movie with id {movie_id} has not seen by the user")

@router.delete(
    '/{movie_id}', 
    response_model=MovieUser,
    response_model_exclude=['id'],
    responses={**HTTP_RESPONSE_404, **HTTP_RESPONSE_500},
    status_code=status.HTTP_200_OK,
    
    summary="Delete a movie from the viewed movies",
)
def delete_movie_user(
    movie_id: int = Path(
        ...,
        title="Movie ID",
        description="This is the movie ID to delete from viewed list",
        example="3",
        ge=1
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
    try:
        return service.delete_movie_user(movie_id=movie_id, user_id=1)
    except NoResultFound:
        not_found(f"The movie with id {movie_id} not exist in viewed movies list for this user")
    except:
        internal_server_error()