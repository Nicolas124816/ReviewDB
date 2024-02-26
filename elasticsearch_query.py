from elasticsearch import Elasticsearch, helpers
import os
import json
import re

with open("secrets.json") as secret:
  auth_json = json.load(secret)
  auth_key = auth_json["elastic_auth_key"]

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", auth_key))

# res = es.search (index="newsgroup", body={"query": {"match": {"doc": "Stanley"}}})
# print(len(res["hits"]["hits"]))
# for doc in res["hits"]["hits"]:
#   print(doc)

# res = es.search (index="newsgroup", body={"query": {"match": {"doc": "Phille"}}})
# print(len(res["hits"]["hits"]))

# res = es.search (index="movie_review", body={"query": {"match": {"doc":{"query": "Phille", "fuzziness": "AUTO"}}}}, size =10000)
# print(len(res["hits"]["hits"]))

res = es.search(index="movie_review", body={"query": {"match": {"comment": "worth"}}})

#res = es.search(index="movie_review", size=1000, body={"query": {"match_all": {}}})

#print(res)
#print(len(res))

print(len(res["hits"]["hits"]))
for doc in res["hits"]["hits"]:
  result = doc["_source"]
  print(result)
  print(f"movie_id = {result['movie_id']}")
  print(f"comment = {result['comment']}")
