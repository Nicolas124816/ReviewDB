import requests
from json import dumps, load, loads

movie_id = 5

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODgzNjM4MWRlN2NkMTg4ZDBlMjRlOThmNDg3NjE4ZCIsInN1YiI6IjY1Yjk2ZGJlMzNhMzc2MDE2Mjg2MzkxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UbB1p6YWO6oAxIHFuq79_u4DVFxYZmX3kO6dWsYN4iM"
}
url = f"https://api.themoviedb.org/3/movie/{movie_id}"
r = requests.get(url, headers=headers)
print(r.status_code)
#print(r.text)
data = loads(r.content)
print(data.keys())
genre = [genre['name'] for genre in data['genres']]
print(genre)


url = 'http://127.0.0.1:8000/moviedata/'
json = load(open('TestMovieData.json'))
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url=url, json=json, headers=headers)
print(r.status_code)
print(r.text)