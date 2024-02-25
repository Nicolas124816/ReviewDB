import json
from json import loads, load
from marshmallow import Schema, fields
from elasticsearch import Elasticsearch, helpers

es = None

class PromptSchema(Schema):
    prompt = fields.String(required=True)
    filters = fields.Integer(required=True) #Bitmapping? allows for future expansion

class AuthorizationSchema(Schema):
    user = fields.String(required=True)
    password = fields.String(required=True)

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
    movie_id_list = list(movie_id_set)

    return json.dumps(movie_id_list)