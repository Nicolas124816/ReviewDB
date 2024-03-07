import requests
import json
from json import loads, load, dumps
from marshmallow import Schema, fields
from elasticsearch import Elasticsearch, helpers
import random

es = None

class PromptSchema(Schema):
    prompt = fields.String(required=True)
    adult = fields.Boolean(required=True) 
    
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
    print("Entered update")
    
    return {"Update": "True"}


def prompt_script(json_str:str):
    """ Your Function that Requires JSON string"""

    movie_id_set = set()

    a_dict = loads(json_str)

    prompt = a_dict["prompt"]

    #if es is None:
    es = initialize_elasticsearch_connection()

    res = es.search(index="movie_review", size=8, body={"query": {"match": {"comment": prompt}}})

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
    print("Entered movie_data_script")

    a_dict = loads(json_str)

    result = {"movies": []}

    movie_list = a_dict["id_list"]
    for movie_id in movie_list:
        
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODgzNjM4MWRlN2NkMTg4ZDBlMjRlOThmNDg3NjE4ZCIsInN1YiI6IjY1Yjk2ZGJlMzNhMzc2MDE2Mjg2MzkxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UbB1p6YWO6oAxIHFuq79_u4DVFxYZmX3kO6dWsYN4iM",
        }
        url_movie = f"https://api.themoviedb.org/3/movie/{movie_id}"
        url_crew = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
        url_review = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US"
        r_movie = requests.get(url_movie, headers=headers)
        r_crew = requests.get(url_crew, headers=headers)
        r_review = requests.get(url_review, headers=headers)
        data_movie = loads(r_movie.content)
        data_crew = loads(r_crew.content)
        data_review = loads(r_review.content)
        
        if data_movie['poster_path'] is not None:
            movie_data = {
                "budget": data_movie['budget'],
                "director": [p['name'] for p in data_crew['crew'] if p['job'] == 'Director'],
                "forAdults": data_movie['adult'],
                "genre": [genre['name'] for genre in data_movie['genres']],
                "overview": data_movie['overview'],
                "posterPath": "https://image.tmdb.org/t/p/w500/"+data_movie['poster_path'],
                "releaseDate": data_movie['release_date'],
                "reviews": [{'author': r['author'], 'content': r['content']} for r in data_review['results'][:min(5, len(data_review['results']))]],
                "runtime": data_movie['runtime'],
                "score": random.randint(0, 100), # TODO fix score, what is score???
                "tagline": data_movie['tagline'],
                "title": data_movie['title'],
                "voteAverage": data_movie['vote_average'],
                "voteCount": data_movie['vote_count']
            }

            result["movies"].append(movie_data)

    return dumps(result)