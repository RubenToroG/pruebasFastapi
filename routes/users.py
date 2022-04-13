import email
from common.common_exceptions import internal_server_error, not_found
from fastapi import APIRouter, Path, status, HTTPException, Body
from movies import services
from users import User, UserService, CreateUser
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
    description="This is the user ID",
    example="5"
    )):
    """
    Documentación...
    
    """
    try:
        user = service.get_user_by_id(user_id)
        return user
    except NoResultFound:
        not_found(detail=f'User with id {user_id} not found')
    except:
        internal_server_error()
    #if(user is None):
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"¡This movie not exist!")
    #return user


@router.post("/new") # Creacion de un usuario nuevo
def create_user(user: CreateUser): # Con el triple punto defino que el parameter_body(user: User) es obligatorio
    return service.create_user(user)