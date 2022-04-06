#Python
import email
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#Models
class User(BaseModel):
    email: str
    nick_name: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None 
    profile_picture: Optional[str] = None #null

@app.get('/')
def home():
    return {'Hello': 'World'}


    #Request and Response Body
@app.post('/user/new')
def create_user(user: User = Body(...)):
    return user

# ... dentro de fastapi, los 3 puntos indican que el parametro es obligatorio

@app.get('/user/detail')
def show_user(
    first_name: Optional[str] = Query(None, min_length=1, max_length=25),
    email: str = Query(...)
):
    return {first_name: email}