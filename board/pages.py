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
    request_data = request.json
    schema_prompt = PromptSchema()
    try:
        result_prompt = schema_prompt.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_prompt = dumps(result_prompt)

    response_prompt = prompt_script(json_prompt)

    schema_data = MovieListSchema()
    try:
        result_data = schema_data.loads(response_prompt) # TODO test, if fails change loads to load
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_data = dumps(result_data)

    response_data = movie_data_script(json_data)
    #response_data.headers.add("Access-Control-Allow-Origin", "http://localhost:4200")
    #response_data.headers.add("Access-Control-Allow-Headers", "Content-Type")
    #response_data.headers.add("Access-Control-Allow-Methods", "POST")

    return jsonify(response_data), 200