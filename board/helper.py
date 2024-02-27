import requests
import json
from json import loads, load, dumps
from marshmallow import Schema, fields
from elasticsearch import Elasticsearch, helpers

es = None

class PromptSchema(Schema):
    prompt = fields.String(required=True)
    filters = fields.Integer(required=True) #Bitmapping? allows for future expansion

class AuthorizationSchema(Schema):
    user = fields.String(required=True)
    password = fields.String(required=True)

class MovieListSchema(Schema):
    id_list = fields.List(fields.Integer(), required=True)

def authorization_check(json_str:str):
    """ Your Function that Requires JSON string"""
    prompt = loads(json_str)
    auth_filename = "AuthorizedUsers.json"
    auth_file = open(auth_filename)
    auth_json = load(auth_file)

    prompt_user = prompt['user']
    prompt_password = prompt['password']

    auth = False
    if prompt_user in auth_json['auth_users']:
        if auth_json['auth_users'][prompt_user] == prompt_password:
            auth = True

    return auth

def initialize_elasticsearch_connection():
    with open("secrets.json") as secret:
        auth_json = load(secret)
        auth_key = auth_json["elastic_auth_key"]

    es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", auth_key))

    return es

def update_script():
    
    # Add Update code here
    
    return {"Update": "True"}


def prompt_script(json_str:str):
    """ Your Function that Requires JSON string"""

    movie_id_set = set()

    a_dict = loads(json_str)

    prompt = a_dict["prompt"]

    #if es is None:
    es = initialize_elasticsearch_connection()

    res = es.search(index="movie_review", size=20, body={"query": {"match": {"comment": prompt}}})

    print(len(res["hits"]["hits"]))
    for doc in res["hits"]["hits"]:
        result = doc["_source"]
        movie_id = result["movie_id"]

        movie_id_set.add(movie_id)

    # convert set to list
    movie_id_list = {"id_list": list(movie_id_set)}

    return dumps(movie_id_list)


def movie_data_script(json_str:str):
    """ Your Function that Requires JSON string"""

    a_dict = loads(json_str)

    result = {"movies": []}

    movie_list = a_dict["id_list"]
    for movie_id in movie_list:
        
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODgzNjM4MWRlN2NkMTg4ZDBlMjRlOThmNDg3NjE4ZCIsInN1YiI6IjY1Yjk2ZGJlMzNhMzc2MDE2Mjg2MzkxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UbB1p6YWO6oAxIHFuq79_u4DVFxYZmX3kO6dWsYN4iM"
        }
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        r = requests.get(url, headers=headers)
        data = loads(r.content)

        movie_data = {
            "budget": data['budget'],
            "director": 'TODO', # TODO fix director
            "forAdults": data['adult'],
            "genre": [genre['name'] for genre in data['genres']],
            "overview": data['overview'],
            "posterPath": data['poster_path'],
            "releaseDate": data['release_date'],
            "reviews": 'TODO', # TODO fix reviews
            "runtime": data['runtime'],
            "score": 'TODO', # TODO fix score, what is score???
            "tagline": data['tagline'],
            "title": data['title'],
            "voteAverage": data['vote_average'],
            "voteCount": data['vote_count'],
            "year": 'TODO' # TODO year or release date???
        }

        result["movies"].append(movie_data)

    return dumps(result)