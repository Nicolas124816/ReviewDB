from elasticsearch import Elasticsearch, helpers
import os
import json
import re

es = Elasticsearch('https://localhost:9200', ca_certs="http_ca.crt", basic_auth=("elastic", "2gK5ssxMs4xgDxCCclAV"))

# res = es.search (index="newsgroup", body={"query": {"match": {"doc": "Stanley"}}})
# print(len(res["hits"]["hits"]))
# for doc in res["hits"]["hits"]:
#   print(doc)

# res = es.search (index="newsgroup", body={"query": {"match": {"doc": "Phille"}}})
# print(len(res["hits"]["hits"]))

# res = es.search (index="newsgroup", body={"query": {"match": {"doc":{"query": "Phille", "fuzziness": "AUTO"}}}}, size =10000)
# print(len(res["hits"]["hits"]))

#res = es.search(index="movie_review", body={"query": {"match": {"doc": "OUTSTANDING"}}})

res = es.search(index="movie_review", size=1000, body={"query": {"match_all": {}}})

#print(res)
#print(len(res))

print(len(res["hits"]["hits"]))
for doc in res["hits"]["hits"]:
  print(doc)
