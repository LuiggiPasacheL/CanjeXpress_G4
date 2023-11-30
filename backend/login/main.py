import os, threading, time
from flask import Flask, request, jsonify
from application.login_service import LoginService, LoginStatus
from application.ports.user_repository import UserRepository
from application.user_service import UserService
from infrastructure.adapters.postgres_user_repository import PostgresUserRepository
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt, unset_jwt_cookies
from alembic import command
from alembic.config import Config

from infrastructure.canje_ms_consumer import consume_message

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'test')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 172800 # 2 days
jwt = JWTManager(app)

userRepository = PostgresUserRepository()
login_service = LoginService(userRepository)
user_service = UserService(userRepository)

@app.route('/validate/admin', methods=['GET'])
@jwt_required()
def validate_admin():
    current_user = get_jwt()
    if current_user['is_admin']:
        response = {
            'success': True,
            'message': 'OK',
            'data': current_user
        }
        return jsonify(response), 200
    else:
        return {"success": False, "message": "NOTFOUND"}, 401

@app.route('/validate', methods=['GET'])
@jwt_required()
def validate():
    current_user = get_jwt()
    response = {
        'success': True,
        'message': 'OK',
        'data': current_user
    }
    return jsonify(response), 200

@app.route('/user-data', methods=['GET'])
@jwt_required()
def get_user_data():
    current_user = get_jwt()
    id = current_user['id']
    user_data = user_service.get_user(id)
    if user_data is None:
        return {"success": False, "message": "NOTFOUND"}, 401
    else:
        return {"success": True, "message": "OK", "data": user_data}, 200

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data.get('username')
        password = req_data.get('password')
        result, dict_user_data = login_service.login(username, password)
        if result == LoginStatus.OK:
            # create access token by id, username, points, profile_picture, is_admin
            access_token = create_access_token(identity=username, additional_claims=dict_user_data)
            return {"success": True, "message": "OK",  "access_token": access_token}, 200
        elif result == LoginStatus.BAD_CREDENTIALS:
            return {"success": False, "message": "BADCREDENTIALS"}, 401
        else:
            return {"success": False, "message": "NOTFOUND"}, 401

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    resp = jsonify({"success": True, "message": "OK"})
    unset_jwt_cookies(resp)
    return resp, 200

def start_consumer(userRepository: UserRepository):
    consume_message(userRepository)

if __name__ == '__main__':
    time.sleep(5)

    try:
        path = os.path.dirname(os.path.abspath(__file__))
        alembic_cfg = Config(os.path.join(path, "alembic.ini"))
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        print(e)

    consumer_thread = threading.Thread(target=start_consumer, args=(userRepository,))
    consumer_thread.start()

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
