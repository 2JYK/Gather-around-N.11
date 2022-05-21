from datetime import datetime, timedelta
from functools import wraps
import os
from pathlib import Path
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
    image = request.files['image_give']

    extension = image.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{mytime}'

    save_to = f'/css/img/fish/{filename}.{extension}'
    test = os.path.abspath(__file__)
    print(test)
    parent_path = Path(test).parent
    abs_path = str(parent_path) + save_to

    image.save(abs_path)

    # user = db.user.find_one({'_id': ObjectId(user['id'])})

    doc = {
        'image': abs_path,
        # 'user_id': user
    }
    db.image.insert_one(doc)
    return jsonify({'result': 'success'})

# @app.route("/upload", methods=['POST'])
# def upload_image():
#     data = json.loads(request.data)

#     image_receive = data.get('image')
#     if image_receive == '':
#         return jsonify({'msg': 'No image'})
#     else:
#         image = request.files['image_receive']
#         # 확장자 추출
#         extension = image.filename.split('.')[-1]
#         # 지금 시간 추출
#         today = datetime.now()
#         # 파일명이 겹치지 않도록 하기 위해 날짜를 입력해준다!
#         mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
#         filename = f'{mytime}'
#         save_to = f'/css/img/{filename}.{extension}'
#         # 파일 저장!
#         image.save(save_to)
#         print(image)

#     # user = db.user.find_one({'_id': ObjectId(user['id'])})

#     doc = {
#         'image': image,
#         # 'user_id': user
#     }
#     db.image.insert_one(doc)

#     return jsonify({'msg': 'success'})
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
    image = list(db.image.find())[-1]  # 54번의 임시버전
    print(image)

    # image = db.image.find_one({'_id': ObjectId(user.get('id'))}) #실험
    # image = db.image.find({'_id': ObjectId(user.get('id'))})[-1]
    # image = db.image.find_one()[-1]
    # image = db.image.find()[-1]
    # image = list(db.image.find())[-1]
    # image = list(db.image.find({'_id': ObjectId(user.get('id'})) #실험
    image["_id"] = str(image["_id"])
    return jsonify({'msg': '성공', 'image': image})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
