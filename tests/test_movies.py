from urllib import response
from fastapi.testclient import TestClient
import main 

client = TestClient(main.app)
MOVIES_ENDPOINT = '/movies/'
STUDIO_GHIBLI_MOVIES = ['Castle in the Sky', 
'Grave of the Fireflies', 
'My Neighbor Totoro', 
'Kiki\'s Delivery Service', 
'Only Yesterday', 
'Porco Rosso', 
'Pom Poko', 
'Whisper of the Heart', 
'Princess Mononoke', 
'My Neighbors the Yamadas', 
'Spirited Away', 
'The Cat Returns', 
'Howl\'s Moving Castle', 
'Tales from Earthsea', 
'Ponyo', 
'Arrietty', 
'From Up on Poppy Hill', 
'The Wind Rises', 
'The Tale of the Princess Kaguya', 
'When Marnie Was There', 
'The Red Turtle', 
'Earwig and the Witch'].sort()

def test_read_all_movies():
    response = client.get(MOVIES_ENDPOINT)
    assert response.status_code == 200
    api_movies = [movie['title'] for movie in response.json()].sort()    
    assert api_movies == STUDIO_GHIBLI_MOVIES

def test_read_movie_id():
    all_movies = client.get(MOVIES_ENDPOINT).json()
    movie_id = all_movies[0]['id']
    response = client.get(f"{MOVIES_ENDPOINT}{movie_id}")
    assert response.json() == all_movies[0]

def test_not_exist_movie():
    response = client.get(f"{MOVIES_ENDPOINT}{99999999}")
    assert response.status_code == 404
    json = response.json()
    assert 'detail' in json
    assert json['detail'] != "" and json['detail'] != None

def test_negative_movie():
    response = client.get(f"{MOVIES_ENDPOINT}{-1}")
    assert response.status_code == 422
    json = response.json()
    assert 'detail' in json
    assert json['detail'] != "" and json['detail'] != None

def test_zero_id_movie():
    response = client.get(f"{MOVIES_ENDPOINT}{0}")
    assert response.status_code == 422
    json = response.json()
    assert 'detail' in json
    assert json['detail'] != "" and json['detail'] != None

def test_decimal_id_movie():
    response = client.get(f"{MOVIES_ENDPOINT}{1.2}")
    assert response.status_code == 422
    json = response.json()
    assert 'detail' in json
    assert json['detail'] != "" and json['detail'] != None

def test_no_numeric_id_movie():
    response = client.get(f"{MOVIES_ENDPOINT}aaaa")
    assert response.status_code == 422
    json = response.json()
    assert 'detail' in json
    assert json['detail'] != "" and json['detail'] != None