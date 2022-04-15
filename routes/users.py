import email
from common.common_exceptions import internal_server_error, not_found
from fastapi import APIRouter, Path, status, HTTPException, Body
from movies import services
from users import User, UserService, CreateUser, UpdateUser
from typing import List
from sqlalchemy.orm.exc import NoResultFound



router = APIRouter(
    prefix="/user",
    tags=["user"]
)

service = UserService()

@router.get(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    summary="Return a user for the indicated id"
    )
async def get_user_by_id(user_id: int = Path(
    ..., 
    title="User Id",
    description="This is the user id",
    example="1"
    )):
    """
    Return user information for the provided user id
    
    """
    try:
        return service.get_user_by_id(user_id)
    except NoResultFound:
        not_found(detail=f'User with id {user_id} not found')
    except:
        internal_server_error()


@router.post(
    '/new',
    summary="Create a user"
    ) # Creacion de un usuario nuevo
def create_user(user: CreateUser): 
    """
    This path operation is used for create a new user
    """
    return service.create_user(user)


@router.put(
    '/{user_id}',
    response_model=User,
    response_model_exclude=['id'],
    status_code=status.HTTP_200_OK,
    summary="Update the user information",
)
def update_user(
    user: UpdateUser,
    user_id 
    ):
    """
    This path operation update the user information
    """
    try:
        return service.update_user(user_id=user_id, user=user)
    except NoResultFound:
        not_found(f"The user with id {user_id} no exist")


@router.delete('/delete/{user_id}')
def delete_user(
    user_id: int = Path(
        ...,
        title="User ID",
        description="Delete a user by ID",
        example="3",
        ge=1
        )
    ):
    try:
        return service.delete_user(user_id=user_id)
    except NoResultFound:
        not_found(f"The user with id {user_id} was delete from de DB")
    except:
        internal_server_error()