from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from pymongo import MongoClient
import jwt, hashlib
from datetime import datetime, timedelta

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route("/")
def hello_word():
    
    return jsonify({'message':'success'})




if __name__ =='__main__':
    app.run('0.0.0.0', port=5000, debug=True)