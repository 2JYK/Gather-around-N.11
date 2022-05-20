import json
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from pymongo import MongoClient
import jwt, hashlib
from datetime import datetime, timedelta

SECRET_KEY = "abcd"

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
client = MongoClient('localhost', 27017)
db = client.gather


# ㅡㅡㅡ 회원가입 ㅡㅡㅡ
@app.route("/sub", methods = ["POST"])
def sign_up():

    data = json.loads(request.data)
    id_receive  = data.get('id')
    password_receive = data.get('password')

# ㅡㅡㅡ 아이디 ㅡㅡㅡ
    if id_receive == '':
        return jsonify({'message':'아이디를 기입해 주세요'})
    elif db.user.find_one({'id':id_receive}):
        return jsonify({'message':'존재하는 아이디 입니다'})
    elif len(str(id_receive)) >= 6:
        id = id_receive
    else:
        return jsonify({'message':'아이디를 6자리 이상 입력해 주세요'})
    

# ㅡㅡㅡ 패스워드 ㅡㅡㅡ
    if password_receive == '':
        return jsonify({'message':'비밀번호 입력해 주세요'})
    elif len(str(password_receive)) >= 8:
        password = password_receive
    else:     
        return jsonify({'message':'비밀번호를 8자리 이상 입력해 주세요'})
    

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

# ㅡㅡㅡ db에 저장 ㅡㅡㅡ
    doc = {
        'id' : id,
        'password' : password_hash
    }
    
    db.user.insert_one(doc)
    return jsonify({'message':'저장완료'})  



# ㅡㅡㅡ 로그인 ㅡㅡㅡ
@app.route("/login", methods=["POST"])    

def login():
    data = json.loads(request.data)

    id = data.get('id')
    password = data.get('password')
    print(password)
    hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

    result = db.user.find_one({
        'id' : id,
        'password' : hashed_pw
    })


    if result is None:
        return jsonify({'message' : '아이디와 비밀번호가 옳바르지 않습니다.'}), 401

# ㅡㅡㅡ 토큰에 싣을 정보 ㅡㅡㅡ
    payload = {
        'id': str(result['_id']),
        'exp': datetime.utcnow() + timedelta(seconds=60*60*24) #로그인 24시간 유지
    }

# ㅡㅡㅡ 토큰발행 ㅡㅡㅡ
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print('86번줄 :', token)

    return jsonify({'message':'로그인 성공!','token':token})







if __name__ =='__main__':
    app.run('0.0.0.0', port=5000, debug=True)