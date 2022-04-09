#FastAPI
from fastapi import FastAPI

#Internal Routes
from routes import movies, movies_user

description = """
API to track studio ghibli viewed movies 

## Users 

(_not implemented_)

## Movies

The API allows:

* **Read movies**

## Movies-User

The API allows:

* **Read viewed movies by the user**
* **Add movie to viewed list**
* **Update user score for the movie**
* **Delete movies from the viewed list**
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Not Implemented",
    },
    {
        "name": "movies",
        "description": "Read movies info",
    },
    {
        "name": "movies-user",
        "description": "Manage viewed movies by the user",
    },
]

app = FastAPI(
    title="Studio ghibli tracker API",
    version="1.0.0",
    description=description,
    openapi_tags=tags_metadata
)

app.include_router(movies.router)
app.include_router(movies_user.router)