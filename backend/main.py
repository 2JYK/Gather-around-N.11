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


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)