from typing import Optional
from pydantic import EmailStr, HttpUrl

from sqlmodel import Field, SQLModel

class BaseUser(SQLModel):
    __tablename__="users"

    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nick_name: Optional[str] = None
    profile_picture: Optional[HttpUrl] = None

class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass