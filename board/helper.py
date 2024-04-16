import requests
import json
from json import loads, load, dumps
from marshmallow import Schema, fields
from elasticsearch import Elasticsearch, helpers
import random

es = None

class PromptSchema(Schema):
    prompt = fields.String(required=True)
    kid = fields.Boolean(required=True) 
    genre = fields.String(required=True)
    rowsOfMovies = fields.Integer(required=True)
    
class AuthorizationSchema(Schema):
    user = fields.String(required=True)
    password = fields.String(required=True)

class MovieListSchema(Schema):
    #id_list = fields.List(fields.Integer(), required=True)
    id_list = fields.Dict(fields.String(required=True), fields.Float(required=True), required=True)
    rows_movies = fields.Integer(required=True)

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


def prompt_script(json_str:str, skip_list):
    """ Your Function that Requires JSON string"""

    movie_id_map = dict()

    a_dict = loads(json_str)
    prompt = a_dict["prompt"]
    rows_of_movies = a_dict["rowsOfMovies"]

    #if es is None:
    es = initialize_elasticsearch_connection()
    size = 4 * rows_of_movies

    res = es.search(
        index="movie_review", size=size, 
        body={"query": {"bool":{
            "must":{"match": {"comment": {"query": prompt, "fuzziness": "AUTO"}}}, 
            "must_not": {"terms": {"movie_id" : skip_list}}
        }}}
    )

    index = 0
    for doc in res["hits"]["hits"]:
        if index >= size - 4:
            score = doc["_score"]
            result = doc["_source"]
            movie_id = result["movie_id"]

            #movie_id_set.add(movie_id)
            movie_id_map[movie_id] = score
        index += 1
        
    # convert set to list
    movie_id_list = {"id_list": movie_id_map, "rows_movies": rows_of_movies}
    

    return dumps(movie_id_list)


def movie_data_script(json_str:str): 
    """ Your Function that Requires JSON string"""
    #print("Entered movie_data_script")

    a_dict = loads(json_str)

    result = {"movies": []}

    movie_list = a_dict["id_list"]

    # # Calculate the max value of score.
    # max_score = 0
    # for movie_id in movie_list:
    #     score = movie_list[movie_id]
    #     if score > max_score:
    #         max_score = score

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
        
        movie_data = {
            "budget": data_movie.get('budget', 'unknown'),
            "director": [p['name'] for p in data_crew.get('crew', []) if p['job'] == 'Director'],
            "forAdults": not bool([m for m in data_movie.get('genres', []) if "Family"==m["name"]]),
            "genre": [genre['name'] for genre in data_movie.get('genres', [])],
            "overview": data_movie.get('overview', 'unkown'),
            "posterPath": "https://image.tmdb.org/t/p/w500/"+data_movie.get('poster_path', 'https://image.tmdb.org/t/p/original/lRQiJXETkCnVVurHmglNvMXrZOx.jpg'),
            "releaseDate": data_movie.get('release_date', 'unknown'),
            "reviews": [{'author': r['author'], 'content': r['content']} for r in data_review.get('results', [])[:min(5, len(data_review.get('results', [])))]],
            "runtime": data_movie.get('runtime', 'unknown'),
            "score": "{:.4f}".format(movie_list[movie_id]),
            "tagline": data_movie.get('tagline', 'unknown'),
            "title": data_movie.get('title', 'untitled'),
            "voteAverage": data_movie.get('vote_average', '0'),
            "voteCount": data_movie.get('vote_count', '0'),
        }

        result["movies"].append(movie_data)

    return dumps(result)
