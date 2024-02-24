from json import loads, load
from marshmallow import Schema, fields


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

def update_script():
    
    # Add Update code here
    
    return {"Update": "True"}

def prompt_script(json_str:str):
    """ Your Function that Requires JSON string"""

    a_dict = loads(json_str)

    # Add Elastic Search code here

    return a_dict