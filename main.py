#FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Internal Routes
from routes import movies, movies_user, users

description = """
API to track studio ghibli viewed movies 

## Users 

The API allows

* **Create a user**
* **Read information from a user**
* **Update user information**

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
        "name": "user",
        "description": "Read user info",
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

#Enable CORS for especified origins
cors_origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(movies_user.router)