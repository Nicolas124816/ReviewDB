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
    print(request_data)
    schema_prompt = PromptSchema()
    try:
        result_prompt = schema_prompt.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    json_prompt = dumps(result_prompt)
    kid_filter = result_prompt["kid"]
    genre_filter = result_prompt["genre"]
    rows_of_movies = result_prompt["rowsOfMovies"]

    response, code = filterLoop(json_prompt, kid_filter, genre_filter, rows_of_movies)

    return response, code

def filterLoop(json_prompt, kid_filter, genre_filter, rows_of_movies):
    skip_list = []
    
    if kid_filter and bool(genre_filter):
        filter_movies = []
        print("Filter Movies")
        while len(filter_movies) < 4:
            temp_response_prompt,temp_response_data, _ = final_script(json_prompt, skip_list)
            temp_movies = loads(temp_response_data)
            temp_id = loads(temp_response_prompt)

            for m in temp_movies["movies"]:
                if len(filter_movies) >= 4:
                    break
                if not m["forAdults"] and genre_filter in m["genre"]:
                    print(m["title"])
                    print(m["genre"])
                    filter_movies.append(m)
            
            skip_list += temp_id["id_list"]

        response_data = dumps({"movies": filter_movies})
        code = 200
    
    elif kid_filter:
        filter_movies = []
        print("Filter Movies")
        while len(filter_movies) < 4:
            temp_response_prompt,temp_response_data, _ = final_script(json_prompt, skip_list)
            temp_movies = loads(temp_response_data)
            temp_id = loads(temp_response_prompt)
           
            for m in temp_movies["movies"]:
                if len(filter_movies) >= 4:
                    break
                if not m["forAdults"]: 
                    print(m["title"])
                    print(m["genre"])
                    filter_movies.append(m)
                    
            skip_list += temp_id["id_list"]

        response_data = dumps({"movies": filter_movies})
        code = 200
   
    elif bool(genre_filter):
        filter_movies = []
        print("Filter Movies")
        while len(filter_movies) < 4:
            temp_response_prompt,temp_response_data, _ = final_script(json_prompt, skip_list)
            temp_movies = loads(temp_response_data)
            temp_id = loads(temp_response_prompt)
            
            for m in temp_movies["movies"]:
                if len(filter_movies) >= 4:
                    break
                if genre_filter in m["genre"]: 
                    print(m["title"])
                    print(m["genre"])
                    filter_movies.append(m)
            
            skip_list += temp_id["id_list"]

        response_data = dumps({"movies": filter_movies})
        code = 200

    else:
        _, response_data, code = final_script(json_prompt, skip_list)

    response = jsonify(response_data)
    return response, code

def final_script(json_prompt, skip_list):
    response_prompt = prompt_script(json_prompt, skip_list)

    schema_data = MovieListSchema()
    try:
        result_data = schema_data.loads(response_prompt) # TODO test, if fails change loads to load
    except ValidationError as err:
        return None, jsonify(err.messages), 400
    
    json_data = dumps(result_data)

    response_data = movie_data_script(json_data)
    #response = jsonify(response_data)

    return response_prompt, response_data, 200