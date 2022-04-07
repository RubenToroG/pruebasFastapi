import datetime as _dt
import pydantic as _pydantic

class _BaseUser(_pydantic.BaseModel):
    email: str
    first_name: str
    last_name: str
    nick_name: str
    profile_picture: str

class User(_BaseUser):
    id: int
    date_created: _dt.date

class CreateUser(_BaseUser):
    pass