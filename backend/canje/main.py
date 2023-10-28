import os
from flask import Flask, request, jsonify
from application.canje_service import CanjeService
from infrastructure.adapters.postgres_user_repository import PostgresUserRepository
from infrastructure.adapters.postgres_product_repository import PostgresProductRepository
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

user_repository = PostgresUserRepository()
product_repository = PostgresProductRepository()

canje_service = CanjeService(user_repository, product_repository)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/canjear', methods=['POST'])
def canjear():
    req_data = request.get_json()
    user_id = req_data.get('user_id')
    cart = req_data.get('cart')
    result = canje_service.canjear(user_id, cart)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))
