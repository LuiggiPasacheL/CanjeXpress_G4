import os

from flask import Flask, request, jsonify
from application.login_service import LoginService, LoginStatus
from infrastructure.adapters.postgres_user_repository import PostgresUserRepository
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from alembic import command
from alembic.config import Config

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'test')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
jwt = JWTManager(app)

login_service = LoginService(PostgresUserRepository())


@app.route('/validate', methods=['GET'])
@jwt_required()
def index():
    current_user = get_jwt_identity()
    return jsonify(username=current_user), 200

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data.get('username')
        password = req_data.get('password')
        result = login_service.login(username, password)
        if result == LoginStatus.OK:
            access_token = create_access_token(identity=username)
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
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
