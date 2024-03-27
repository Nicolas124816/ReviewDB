from flask_cors import cross_origin
import requests
from flask import Blueprint, render_template, request, jsonify
from json import dumps, loads
from marshmallow import Schema, fields, ValidationError
from board.helper import *


bp = Blueprint("pages", __name__)

@bp.get("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.post("/update/")
def update():
    request_data = request.json
    schema = AuthorizationSchema()
    try:
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    request_json = dumps(result)

    if authorization_check(request_json):
        response_data = update_script()
        return jsonify(response_data), 200
    else:
        return jsonify({"Update" : "False"}), 400 #Needs to be updated

@bp.post("/prompt/")
def prompt():
    request_data = request.json
    schema = PromptSchema()
    try:
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    request_json = dumps(result)

    response_data = prompt_script(request_json)
    

    return jsonify(response_data), 200

@bp.post("/moviedata/")
def movieData():
    request_data = request.json
    schema = MovieListSchema()
    try:
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    request_json = dumps(result)

    response_data = movie_data_script(request_json)

    return jsonify(response_data), 200


@bp.post("/prompt/test/")
@cross_origin()
def promptTest():
    print("Entered API")
    skip_list = []

    request_data = request.json
    schema_prompt = PromptSchema()
    try:
        result_prompt = schema_prompt.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_prompt = dumps(result_prompt)

    if result_prompt["adult"]:
        kids_movies = []
        print("Kids Movies")
        while len(kids_movies) < 8:
            temp_response_prompt,temp_response_data, _ = final_script(json_prompt, skip_list)
            temp_movies = loads(temp_response_data)
            temp_id = loads(temp_response_prompt)
            for m in temp_movies["movies"]:
                if "Family" in m["genre"]: 
                    #print(m["title"])
                    kids_movies.append(m)
            skip_list += temp_id["id_list"]
        #print(skip_list)
        response_data = dumps({"movies": kids_movies})
        code = 200
    else:
        _, response_data, code = final_script(json_prompt, skip_list)

    #print(response_data)
    response = jsonify(response_data)

    return response, code


def final_script(json_prompt, skip_list):
    response_prompt = prompt_script(json_prompt, skip_list)

    schema_data = MovieListSchema()
    try:
        result_data = schema_data.loads(response_prompt) # TODO test, if fails change loads to load
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_data = dumps(result_data)

    response_data = movie_data_script(json_data)
    #response = jsonify(response_data)

    return response_prompt, response_data, 200

'''
@bp.post("/prompt/test/")
@cross_origin()
def promptTest():
    print("Entered API")
    skip_list = []

    request_data = request.json
    schema_prompt = PromptSchema()
    try:
        result_prompt = schema_prompt.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_prompt = dumps(result_prompt)

    if result_prompt["adult"]:

    response_prompt = prompt_script(json_prompt, skip_list)

    schema_data = MovieListSchema()
    try:
        result_data = schema_data.loads(response_prompt) # TODO test, if fails change loads to load
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_data = dumps(result_data)

    response_data = movie_data_script(json_data)
    response = jsonify(response_data)

    return response, 200
'''