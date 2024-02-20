from datetime import date
import requests
import json

def get_date():
    today = date.today()
    return today.strftime("%m_%d_%Y")


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODgzNjM4MWRlN2NkMTg4ZDBlMjRlOThmNDg3NjE4ZCIsInN1YiI6IjY1Yjk2ZGJlMzNhMzc2MDE2Mjg2MzkxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UbB1p6YWO6oAxIHFuq79_u4DVFxYZmX3kO6dWsYN4iM"
}

#get all movie ids from 'TMDB_Comments/movie_ids_' + get_date() + '.json' and store them in a list
movie_ids = []

with open('TMDB_Comments/movie_ids_' + get_date() + '.json', 'r') as f:
    for line in f:
        data = json.loads(line)
        movie_ids.append(data['id'])

id = 11

url = "https://api.themoviedb.org/3/movie/" + str(id) + "/reviews?language=en-US&page=1"
response = requests.get(url, headers=headers)

if response.json()['total_results'] < 0:
    print("No reviews for movie with id " + str(id))
else:
    print(response.json())
    with open('TMDB_Comments/ReviewDatabase.json', 'w') as f:
        json.dump(response.json(), f)