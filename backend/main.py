from datetime import datetime, timedelta
from functools import wraps
from bson import ObjectId
from pymongo import MongoClient
from flask import Flask, abort, jsonify, request
import hashlib
import json
from flask_cors import CORS
import jwt


app = Flask(__name__)
# 현재는 테스트 서버에서 돌려서 origins에 모든 것을 다 받아오는 *를 썼지만, 나중에 서비스를 하게 된다면 원하는 프론트에서만 받도록 설정해야 함
cors = CORS(app, resources={r"*": {"origins": "*"}})
client = MongoClient('localhost', 27017)
db = client.fish

SECRET_KEY = 'turtle'


@app.route("/upload", methods=['POST'])
def upload_image():
    data = json.loads(request.data)

    image_receive = data.get('image')
    print(image_receive)
    # user = db.user.find_one({'_id': ObjectId(user['id'])})

    doc = {
        'image': image_receive,
        # 'user_id': user
    }
    db.image.insert_one(doc)

    return jsonify({'msg': 'success'})
# ######################
# @app.route("/article", methods=["GET"])
# def get_article():
#     articles = list(db.article.find())  
#     # print(articles) 
#     for article in articles:
#         # print(article.get("title")) 
#         article["_id"] = str(article["_id"])
#     return jsonify({'msg':'success', 'articles':articles})
    
####################

@app.route("/upload", methods=['GET'])
# @authorize
def show_image():   # ()안에 user
    image = list(db.image.find())[-1] #54번의 임시버전
    print(image)
    
    # image = db.image.find_one({'_id': ObjectId(user.get('id'))}) #실험
    # image = db.image.find({'_id': ObjectId(user.get('id'))})[-1] 
    # image = db.image.find_one()[-1] 
    # image = db.image.find()[-1] 
    # image = list(db.image.find())[-1]
    # image = list(db.image.find({'_id': ObjectId(user.get('id'})) #실험
    image["_id"] = str(image["_id"])
    return jsonify({'msg': '성공', 'image':image})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)