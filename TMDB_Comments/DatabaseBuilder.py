from datetime import date
import requests
import json

def get_date():
    today = date.today()
    return today.strftime("%m_%d_%Y")

def write_to_database(comment, movie_id):
    # write the comment andm ovie id to the database in json format
    with open('TMDB_Comments/Database.json', 'a') as f:
        f.write(json.dumps({"movie_id": movie_id, "comment": comment}) + '\n')
        f.close()


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

id = 331

url = "https://api.themoviedb.org/3/movie/" + str(id) + "/reviews?language=en-US&page=1"
response = requests.get(url, headers=headers)

if response.json()['total_results'] < 0:
    print("No reviews for movie with id " + str(id))
else:
    print(response.json())
    # add just the comment content and movie id to the database
    for review in response.json()['results']:
        write_to_database(review['content'], id)



