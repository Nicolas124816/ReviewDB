from datetime import date
from fileinput import filename
import time
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

filename = 'TMDB_Comments/DailyExport/movie_ids_02_27_2024.json'

with open(filename, 'r', encoding="utf8") as f:
    for line in f:
        data = json.loads(line)
        movie_ids.append(data['id'])
        
#print(movie_ids.index(645124))
#time.sleep(50)
        
# get the comments for each movie id and write them to the database
counter = 455940
for id in movie_ids[455940:]:

    while True:
        try:
            url = "https://api.themoviedb.org/3/movie/" + str(id) + "/reviews?language=en-US&page=1"
            response = requests.get(url, headers=headers)
            break
        except:
            print("Connection error, retrying in 10 seconds")
            time.sleep(10)
            continue

    if response.status_code != 200:
        print("Error: " + str(response.status_code))
        continue
    else:
        if response.json()['total_results'] <= 0:
            print("No reviews for movie with id " + str(id))
        else:
            # create json list with author names and their review content
            reviews = []
            for review in response.json()['results']:
                reviews.append({str(review['author']): review['content']})

            with open('TMDB_Comments/ReviewDatabase.json', 'a') as f:
                f.write(json.dumps({"movie_id": id, "comments:": reviews}) + '\n')
                f.close()
    counter += 1
    print(counter)
    time.sleep(0.03)





 