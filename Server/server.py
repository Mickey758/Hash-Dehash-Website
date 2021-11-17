from threading import Lock
lock = Lock()

from handler import *

from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/hash*": {"origins": "*"},r"/dehash*": {"origins":"*"}})

@app.route("/hash",methods=["POST"])
def hash_page():
    if not request.json:
        return "Need json format: {'text':'Hello World!'}"

    text = request.json.get("text")
    if not text:
        return "Missing Text"

    return add_hash(text)

@app.route("/dehash",methods=["POST"])
def dehash_page():
    if not request.json:
        return "Need json format: {'hash':'Hello World!'}"

    text = request.json.get("hash")
    if not text:
        return "Missing Hash"
    
    return get_hash(text)

app.run("0.0.0.0",5000)