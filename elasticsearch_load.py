from elasticsearch import Elasticsearch, helpers
import os
import json
import re

with open("secrets.json") as secret:
    auth_json = json.load(secret)
    auth_key = auth_json["elastic_auth_key"]

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", auth_key))


with open("TMDB Reviews Datasets/tmdb_movies_data.json") as file:
    docs = json.loads(file.read())
    #print(docs)
    helpers.bulk(es, docs)
    
with open("TMDB Reviews Datasets/tmdb-movies-reviews.json") as file:
    docs = json.loads(file.read())
    #print(docs)
    helpers.bulk(es, docs)
