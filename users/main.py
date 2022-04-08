# Python
from typing import Optional               # Creacion de tipado estatico
from enum import Enum                     # Crea enumeraciones de Strings

# Pydantic
from pydantic import BaseModel            # Clase de pydantic para creacion de los modelos
from pydantic import Field   
from pydantic import EmailStr   
from pydantic import SecretStr         # 

# FastAPI
from fastapi import FastAPI               #
from fastapi import Body, Query, Path     #

app = FastAPI()

# ==============================================================================================================
# Models

class Score(BaseModel):
    id_score: int = Field(
        default=None,
        it=100000
    )
    id_user: int
    id_movie: int
    user_score: float = Field(
        default=None,
        le=10
    )

class User(BaseModel):
    id_user: int = Field(
        gt=0,
        it=100000
    )
    email: EmailStr = Field(...)
    first_name: str = Field(
        ..., 
        min_length=1, 
        max_length=15
    )
    last_name: str = Field(
        ..., 
        min_length=1, 
        max_length=20
    )
    password: SecretStr
    profile_picture: str
    nick_name: Optional[str] = None # Ponemos "Optional" cuando el atributo de la tabla no es obligatorio y "None" es el valor por defecto

# ==============================================================================================================


# @app.get("/") # Este es una Path Operations del METODO "get" que viene del OBJETO "app" que es una instancia de FastAPI
# def home():
#     return {"Hello": "World"}


# Request and Response Body

@app.post("/users/new") # Creacion de un usuario nuevo
def create_user(user: User = Body(...,)): # Con el triple punto defino que el parameter_body(user: User) es obligatorio
    return user


# Validaciones: Path Parameters

@app.get("/users/detail/{id_user}")
def show_user(
    id_user: int = Path(
        ...,
        gt=0,
        it=100000,
        title="User ID",
        description="This is the user ID. It's between 1 and 100000 characters"
    )
):
    return {id_user: "It Exists!"}

# Validacines: Request Body

@app.put("/users/update/{id_user}")
def update_user(
    id_user: int = Path(
        ...,
        title="User ID",
        description="This is the user ID",
        gt=0,
        it=100000
    ),
    user: User = Body(...),
    score: Score = Body(...)
):
    results = user.dict()
    results.update(score.dict())
    return results


@app.delete("/users/delete/{id_user}")
def delete_user(
    id_user: int = Path(
        ...,
        title="User ID",
        description="This is the user ID",
        gt=0,
        it=100000
    ),
    user: User = Body(...),
    score: Score = Body(...)
):
    return ("User Delete")
