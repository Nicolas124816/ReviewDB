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

# Get the movie id change list from https://api.themoviedb.org/3/movie/changes 
url = "https://api.themoviedb.org/3/movie/changes?page=1"
response = requests.get(url, headers=headers)
page_count = response.json()['total_pages']

# Get the movie ids from the response
ids_to_add = []
for change in response.json()['results']:
    ids_to_add.append(change['id'])

for i in range(2, page_count + 1):
    try:
        url = "https://api.themoviedb.org/3/movie/changes?page=" + str(i)
        response = requests.get(url, headers=headers)
        for change in response.json()['results']:
            ids_to_add.append(change['id'])
    except:
        print("Connection error, retrying in 10 seconds")
        time.sleep(10)
        continue


if len(ids_to_add) == 0:
    print("No new movies to add")
    exit()

print("Adding " + str(len(ids_to_add)) + " new movies")


exit()
# get the comments for each movie id and write them to the database
counter = 0
for id in ids_to_add:

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
    time.sleep(0.02)