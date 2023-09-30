from flask import Flask, request, jsonify
from app.login.application.login_service import LoginService

app = Flask(__name__)
login_service = LoginService()

@app.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    result = login_service.login(username, password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
