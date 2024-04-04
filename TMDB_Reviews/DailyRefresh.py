from datetime import date
from fileinput import filename
import time
import requests
import json
import sys

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.6+
    count = len(it)
    start = time.time()
    def show(j):
        x = int(size*j/count)
        remaining = ((time.time() - start) / j) * (count - j)
        
        mins, sec = divmod(remaining, 60)
        time_str = f"{int(mins):02}:{sec:05.2f}"
        
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)
        
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

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

# Get all the movie ids currently in the review database
movie_ids = []

filename = 'TMDB_Reviews/ReviewDatabase.json'

with open(filename, 'r', encoding="utf8") as f:
        for line in f:
            data = json.loads(line)
            movie_ids.append(data['movie_id'])

with open(filename, 'r', encoding="utf8") as f:
                    lines = f.readlines()
                    f.close()

# get the comments for each movie id and write them to the database
counter = 0
for id in progressbar(ids_to_add, "Adding new movies: ", 40):

    while True:
        try:
            url = "https://api.themoviedb.org/3/movie/" + str(id) + "/reviews?language=en-US&page=1"
            response = requests.get(url, headers=headers)
            break
        except:
            print("Connection error, retrying in 10 seconds\n")
            time.sleep(10)
            continue

    if response.status_code != 200:
        print("Error: " + str(response.status_code))
        continue
    else:
        if response.json()['total_results'] > 0:
            # create json list with author names and their review content
            reviews = []
            for review in response.json()['results']:
                reviews.append({str(review['author']): review['content']})
            
            # write the reviews to the database, if it already exists, append to it

            if id in movie_ids:
                movie_line = movie_ids.index(id)
                # Only write to the file if the reviews are different
                if lines[movie_line] != json.dumps({"movie_id": id, "comments:": reviews}) + '\n':
                    with open(filename, 'w', encoding="utf8") as f:
                        lines[movie_line] = json.dumps({"movie_id": id, "comments:": reviews}) + '\n'
                        f.writelines(lines)

            else:
                with open(filename, 'a', encoding="utf8") as f:
                    f.write(json.dumps({"movie_id": id, "comments:": reviews}) + '\n')
                    f.close()          

    counter += 1
    time.sleep(0.02)

