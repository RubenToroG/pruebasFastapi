from typing import Optional
from sqlmodel import Field, SQLModel

class BaseUser(SQLModel):
    __tablename__="users"

    email: str
    first_name: str
    last_name: str
    nick_name: str
    profile_picture: str

class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    @classmethod
    def from_dict(cls, values: dict): 
        return cls(
        id = values['id'] if 'id' in values else None,
        email= values['email'],
        first_name= values['first_name'],
        last_name= values['last_name'],
        nick_name= values['nick_name'],
        profile_picture= values['profile_picture'])

class CreateUser(BaseUser):
    pass