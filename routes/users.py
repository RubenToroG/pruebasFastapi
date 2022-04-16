from common.common_exceptions import internal_server_error, not_found
from sqlalchemy.orm.exc import NoResultFound
from users import User, UserService, CreateUser, UpdateUser

from fastapi import APIRouter, Path, status, Body


router = APIRouter(prefix="/user", tags=["user"])
service = UserService()

#GET-----------------------------------------------------------------
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
    Return user information for the user
    
    """
    try:
        return service.get_user_by_id(user_id)
    except NoResultFound:
        not_found(detail=f'User with id {user_id} not found')
    except:
        internal_server_error()


#POST--------------------------------------------------------------------
@router.post('/new', summary="Create a user")
def create_user(user: CreateUser): 
    """
    This path operation is used for create a new user
    """
    return service.create_user(user)


#PUT--------------------------------------------------------------------
@router.put(
    '/{user_id}',
    response_model=User,
    response_model_exclude=['id'],
    status_code=status.HTTP_200_OK,
    summary="Update the user information",
)
def update_user(user: UpdateUser, user_id):
    """
    This path operation update the user information
    """
    try:
        return service.update_user(user_id=user_id, user=user)
    except NoResultFound:
        not_found(f"The user with id {user_id} no exist")


#DELETE----------------------------------------------------------------
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