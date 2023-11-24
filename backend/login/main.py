import os

from flask import Flask, request, jsonify
from application.login_service import LoginService, LoginStatus
from infrastructure.adapters.postgres_user_repository import PostgresUserRepository
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token, get_jwt
from alembic import command
from alembic.config import Config

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'test')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 172800 # 2 days
jwt = JWTManager(app)

login_service = LoginService(PostgresUserRepository())

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
def index():
    current_user = get_jwt()
    response = {
        'success': True,
        'message': 'OK',
        'data': current_user
    }
    return jsonify(response), 200

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

if __name__ == '__main__':
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        alembic_cfg = Config(os.path.join(path, "alembic.ini"))
        command.upgrade(alembic_cfg, "head")
    except Exception as e:
        print(e)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
