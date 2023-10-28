import os

from flask import Flask, request, jsonify, render_template
from application.login_service import LoginService
from infrastructure.adapters.postgres_user_repository import PostgresUserRepository
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

login_service = LoginService(PostgresUserRepository())

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data.get('username')
        password = req_data.get('password')
        result = login_service.login(username, password)
        return jsonify(result)

    return 'Login Page with CORS enabled'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))
