import os

from flask import Flask, request, jsonify, render_template
from application.login_service import LoginService
from infrastructure.adapters.postgres_user_repository import PostgresUserRepository

app = Flask(__name__)
login_service = LoginService(PostgresUserRepository())

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'frontend')
template_dir = os.path.join(template_dir, 'templates')
print(f"templates route: {template_dir}")

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data.get('username')
        password = req_data.get('password')
        result = login_service.login(username, password)
        return jsonify(result)
        
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
