#FastAPI
from fastapi import FastAPI

#Internal Routes
from routes import movies, movies_user

app = FastAPI()

app.include_router(movies.router)
app.include_router(movies_user.router)