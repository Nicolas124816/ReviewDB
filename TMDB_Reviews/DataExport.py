# Kush Dalal 2/13/2024

import json
import requests
import gzip
import shutil
from datetime import date
import os


# Access the TMDB api using the api key in config.json
def get_data(url):
    response = requests.get(url)
    return response.json()

# Get the api key from the config file
def get_api_key():
    with open('config.json') as f:
        data = json.load(f)
    return data['tmdb_api_key']

# Get today's date in the format required by the TMDB api
def get_date():
    today = date.today()
    return today.strftime("%m_%d_%Y")

url = "http://files.tmdb.org/p/exports/movie_ids_" + get_date() + ".json.gz?api_key=18836381de7cd188d0e24e98f487618d"


# Download the file from the url
r = requests.get(url)
with open('movie_ids_' + get_date() + '.json.gz', 'wb') as f:
    f.write(r.content)

#clear the DailyExport folder
folder = 'TMDB_Reviews/DailyExport'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

# Unzip the file
with gzip.open('movie_ids_' + get_date() + '.json.gz', 'rb') as f_in:
    with open('TMDB_Reviews/DailyExport/movie_ids_' + get_date() + '.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# delete the zipped file
os.remove('movie_ids_' + get_date() + '.json.gz')

        


