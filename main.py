#FastAPI
from fastapi import FastAPI

#Internal Routes
from routes import movies

app = FastAPI()

app.include_router(movies.movies_router)
app.include_router(movies.movies_user_router)

@app.get('/')
def home():
    return {'Hello': 'World'}