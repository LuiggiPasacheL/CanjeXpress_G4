from flask import Flask, request, jsonify
from app.login.application.login_service import LoginService
import os

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'frontend')
template_dir = os.path.join(template_dir, 'templates')
print(f"templates route: {template_dir}")

app = Flask(__name__, template_folder=template_dir)
login_service = LoginService()

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
