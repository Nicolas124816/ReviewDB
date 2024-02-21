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