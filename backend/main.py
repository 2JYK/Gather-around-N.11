# from functools import wraps
# import json
# from flask import Flask, request, jsonify, abort
# from flask_cors import CORS
# from pymongo import MongoClient
# import jwt
# from bson import ObjectId
# import os
# from pathlib import Path
# import hashlib
# from datetime import datetime, timedelta

# SECRET_KEY = "abcd"

# app = Flask(__name__)
# cors = CORS(app, resources={r'*': {'origins': '*'}})
# client = MongoClient('localhost', 27017)
# db = client.gather

# # ㅡㅡㅡ 전역함수 ㅡㅡㅡ
# # 로컬 저장소에 토큰 값 저장하는 함수
# def authorize(f):
#     @wraps(f)
#     # argument와 key-word argument가 같이 들어가는 경우를 위해 작성
#     # *과 ** 만 있다면 이름은 뒤에 아무거나 붙어도 무방은 함
#     # *args: list 형태로 아무거나 다 들어와 된다.
#     # **kwargs : a = b의 형태로 즉, 키워드의 형태로 몇개씩 들어와도 인식을 하겠다.
#     def decorated_function(*args, **kwargs):
#         # 만약 Authorization이 헤더 안에 없다면
#         if not 'Authorization' in request.headers:
#             abort(401)  # 401 에러를 반환
#         # Authorization이 헤더 안에 있다면 'token' 변수에 저장
#         token = request.headers['Authorization']
#         try:
#             # 토큰을 디코드한 값을 user에 저장
#             # _id, email, exp가 들어있음
#             user = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         except:
#             abort(401)
#         return f(user, *args, **kwargs)
#     return decorated_function

#     # ㅡㅡㅡ 회원가입 ㅡㅡㅡ
# @app.route("/sub", methods=["POST"])
# def sign_up():

#     data = json.loads(request.data)
#     id_receive = data.get('id')
#     password_receive = data.get('password')

# # ㅡㅡㅡ 아이디 ㅡㅡㅡ
#     if id_receive == '':
#         return jsonify({'message': '아이디를 기입해 주세요'})
#     elif db.user.find_one({'id': id_receive}):
#         return jsonify({'message': '존재하는 아이디 입니다'})
#     elif len(str(id_receive)) >= 6:
#         id = id_receive
#     else:
#         return jsonify({'message': '아이디를 6자리 이상 입력해 주세요'})


# # ㅡㅡㅡ 패스워드 ㅡㅡㅡ
#     if password_receive == '':
#         return jsonify({'message': '비밀번호 입력해 주세요'})
#     elif len(str(password_receive)) >= 8:
#         password = password_receive
#     else:
#         return jsonify({'message': '비밀번호를 8자리 이상 입력해 주세요'})

#     password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

# # ㅡㅡㅡ db에 저장 ㅡㅡㅡ
#     doc = {
#         'id': id,
#         'password': password_hash
#     }

#     db.user.insert_one(doc)
#     return jsonify({'message': '저장완료'}), 201

#     # ㅡㅡㅡ 로그인 ㅡㅡㅡ


# @app.route("/login", methods=["POST"])
# def login():
#     data = json.loads(request.data)

#     id = data.get('id')
#     password = data.get('password')

#     hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

#     result = db.user.find_one({
#         'id': id,
#         'password': hashed_pw
#     })

#     if result is None:
#         return jsonify({'message': '아이디와 비밀번호가 옳바르지 않습니다.'}), 401

# # ㅡㅡㅡ 토큰에 싣을 정보 ㅡㅡㅡ
#     payload = {
#         'id': str(result['_id']),
#         'exp': datetime.utcnow() + timedelta(seconds=60*60*24)  # 로그인 24시간 유지
#     }

# # ㅡㅡㅡ 토큰발행 ㅡㅡㅡ
#     token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

#     return jsonify({'message': '로그인 성공!', 'token': token})


# # ㅡㅡㅡ 메인페이지 사진 업로드 ㅡㅡㅡ
# @app.route("/upload", methods=['POST'])
# # @authorize
# def upload_image():
#     # data = request.form['image_give']
#     image = request.files['image_give']
#     # print(image)
#     extension = image.filename.split('.')[-1]
#     today = datetime.now()
#     mytime = today.strftime('%Y%m%d%H%M%S')
#     # print(mytime)
#     filename = f'{mytime}'

#     save_to = f'/css/img/fish/{filename}.{extension}'
#     test = os.path.abspath(__file__)

#     # print(test)
#     parent_path = Path(test).parent
#     # print(f'parent_path는 {parent_path}')
#     abs_path = str(parent_path) + save_to
#     print(abs_path) # 애를 보내줘야함 url부분으로 !

#     image.save(abs_path)

#     # user = db.user.find_one({'_id': ObjectId(user['id'])})


#     doc = {
#         'image': abs_path,
#         # 'user_id': user
#     }
#     db.image.insert_one(doc)
#     return jsonify({'result': 'success', 'abs_path': abs_path})  




# # ㅡㅡㅡ 메인페이지 사진 보여주기 ㅡㅡㅡ
# # @app.route("/upload", methods=['GET'])
# # # @authorize

# # ㅡㅡㅡ 물고기 정보 디비에서 빼오기 ㅡㅡㅡ 본인이 잡은 물고기가 무엇인지 알수 있음 !

# @app.route("/fish/<name_en>", methods=["GET"])
# @authorize
# def fish_detail(user, name_en):
#     print(user, name_en)  
#     fishinfo = db.fish_info.find_one({"name_en": name_en})
#     print(fishinfo)
#     fishinfo["_id"] = str(fishinfo["_id"])
#     user = user["id"]
    
#     return jsonify({'message': 'success', 'user':user, "fishinfo": fishinfo})




# if __name__ == '__main__':
#     app.run('127.0.0.1', port=5000, debug=True)
