from functools import wraps
import json
from bson import ObjectId
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from pymongo import MongoClient
from pathlib import Path
import jwt
import hashlib
from datetime import datetime, timedelta
import os

SECRET_KEY = "abcd"

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
client = MongoClient('localhost', 27017)
db = client.gather

    # ㅡㅡㅡ 전역함수 ㅡㅡㅡ
# 로컬 저장소에 토큰 값 저장하는 함수
def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401)
        token = request.headers['Authorization']
        try:
            user = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except:
            abort(401)
        return f(user, *args, **kwargs)
    return decorated_function


    # ㅡㅡㅡ 회원가입 ㅡㅡㅡ
@app.route("/sub", methods=["POST"])
def sign_up():

    data = json.loads(request.data)
    id_receive = data.get('id')
    password_receive = data.get('password')

# ㅡㅡㅡ 아이디 ㅡㅡㅡ
    if id_receive == '':
        return jsonify({'message': '아이디를 기입해 주세요'})
    elif db.user.find_one({'id': id_receive}):
        return jsonify({'message': '존재하는 아이디 입니다'})
    elif len(str(id_receive)) >= 6:
        id = id_receive
    else:
        return jsonify({'message': '아이디를 6자리 이상 입력해 주세요'})


# ㅡㅡㅡ 패스워드 ㅡㅡㅡ
    if password_receive == '':
        return jsonify({'message': '비밀번호 입력해 주세요'})
    elif len(str(password_receive)) >= 8:
        password = password_receive
    else:
        return jsonify({'message': '비밀번호를 8자리 이상 입력해 주세요'})

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

# ㅡㅡㅡ db에 저장 ㅡㅡㅡ
    doc = {
        'id': id,
        'password': password_hash
    }

    db.user.insert_one(doc)
    return jsonify({'message': '저장완료'}), 201


    # ㅡㅡㅡ 로그인 ㅡㅡㅡ
@app.route("/login", methods=["POST"])
def login():
    data = json.loads(request.data)

    id = data.get('id')
    password = data.get('password')

    hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

    result = db.user.find_one({
        'id': id,
        'password': hashed_pw
    })

    if result is None:
        return jsonify({'message': '아이디와 비밀번호가 옳바르지 않습니다.'}), 401

# ㅡㅡㅡ 토큰에 싣을 정보 ㅡㅡㅡ
    payload = {
        'id': str(result['_id']),
        'exp': datetime.utcnow() + timedelta(seconds=60*60*24)  # 로그인 24시간 유지
    }

# ㅡㅡㅡ 토큰발행 ㅡㅡㅡ
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jsonify({'message': '로그인 성공!', 'token': token})

# ㅡㅡㅡ Diary 유저 정보 확인 ㅡㅡㅡ
@app.route("/getuserinfo", methods=["GET"])
@authorize
def get_user_info(user):
    result = db.user.find_one({
        "_id": ObjectId(user["id"])
    })
    print("110번재:",result)

    return jsonify({"message":"success", "id": result["id"]})


# ㅡㅡㅡ 게시판 api 시작 ㅡㅡㅡ
@app.route("/diary", methods=["GET"])
@authorize
def get_article(user):
    images = list(db.image.find())
    for image in images:
        image["_id"] = str(image["_id"])

    return jsonify({"message":"success", "images":images})
# DB에서 이미지값을 클라에게 보내줌.


# ㅡㅡㅡ 게시판 삭제 ㅡㅡㅡ
@app.route("/dairy", methods=['DELETE'])
@authorize
def delete_article(user,article_id):
    article = db.article.delete_one(
        {"_id":ObjectId(article_id), "user":user["id"]}
    )
    if article.deleted_count:
        return jsonify({"mesage":"success"})







    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅡㅡㅡ 메인페이지 사진 업로드 ㅡㅡㅡ
@app.route("/upload", methods=['POST'])
@authorize
def upload_image(user):

    image = request.files['image_give']
    extension = image.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y%m%d%H%M%S')
    filename = f'{mytime}'

    save_to = f'/fish/{filename}.{extension}'

    image.save(save_to)
     
    doc = {
        'image': save_to,
        'user_id': user
    }
    db.image.insert_one(doc)
    return jsonify({'result': 'success', 'user':user, 'save_to': save_to})  

# 대근버전
# @app.route("/upload", methods=['POST'])
# # @authorize
# def upload_image():

#     image = request.files['image_give']

#     extension = image.filename.split('.')[-1]
#     today = datetime.now()
#     mytime = today.strftime('%Y%m%d%H%M%S')

#     filename = f'{mytime}'

#     save_to = f'backend/fish/{filename}.{extension}'

#     image.save(save_to)
#     save_to = "../" + save_to

#     # user = user['id']

#     doc = {
#         'image': save_to,
#         # 'user_id': user
#     }
#     db.image.insert_one(doc)
#     return jsonify({'result': 'success', 'save_to': save_to})


# ㅡㅡㅡ 물고기 정보 디비에서 빼오기 ㅡㅡㅡ 본인이 잡은 물고기가 무엇인지 알수 있음 !

@app.route("/fish/<string:name_en>", methods=["GET"])
@authorize
def fish_detail(user, name_en):
    user_id = user["id"]
    
    userinfo = db.user.find_one({"_id":ObjectId(user_id)})
    fishinfo = db.fish_info.find_one({"name_en":name_en})
    fishinfo["_id"] = str(fishinfo["_id"])
    
    fishinfoes = userinfo['fishinfo']
    
    fishinfoes.append(str(fishinfo["_id"]))   
    
    db.user.update_one({'_id': ObjectId(user_id)}, {"$set":{'fishinfo': fishinfoes}})
    

    # db.user.insert_one({'_id': ObjectId(user), 'fishinfo': fishinfo})
    #pymongo.errors.DuplicateKeyError: E11000 duplicate key error collection: gather.user index: _id_ dup key: { _id: ObjectId('628a531e6ff79d8e94abba87') }, full error: {'index': 0, 'code': 11000, 'keyPattern': {'_id': 1}, 'keyValue': {'_id': ObjectId('628a531e6ff79d8e94abba87')}, 'errmsg': "E11000 duplicate key error collection: gather.user index: _id_ dup key: { _id: ObjectId('628a531e6ff79d8e94abba87') }"}
    return jsonify({'message': '냠냠', 'user':user, "fishinfo": fishinfo})









if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)