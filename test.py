import requests
from json import dumps, load

url = 'http://127.0.0.1:8000/prompt/'
json = load(open('PromptTest.json'))
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url=url, json=json, headers=headers)
print(r.status_code)
print(r.text)

url = 'http://127.0.0.1:8000/update/'
json = {'user': 'user1', 'password': 'password1'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url=url, json=json, headers=headers)
print(r.status_code)
print(r.text)