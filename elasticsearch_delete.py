from elasticsearch import Elasticsearch, helpers
import os
import json
import re

with open("secrets.json") as secret:
    auth_json = json.load(secret)
    auth_key = auth_json["elastic_auth_key"]

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", auth_key))

es.delete_by_query(index="movie_info", query={"match_all": {}})
es.delete_by_query(index="movie_review", query={"match_all": {}})

#es.delete(index="movie_info")
#es.delete(index="movie_review")
