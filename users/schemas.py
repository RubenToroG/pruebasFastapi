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

    @classmethod
    def from_dict(cls, values: dict): 
        return cls(
        id = values['id'] if 'id' in values else None,
        email= values['email'] if 'email' in values else None,
        first_name= values['first_name'] if 'first_name' in values else None,
        last_name= values['last_name'] if 'last_name' in values else None,
        nick_name= values['nick_name'] if 'nick_name' in values else None,
        profile_picture= values['profile_picture'] if 'profile_picture' in values else None
        )

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass