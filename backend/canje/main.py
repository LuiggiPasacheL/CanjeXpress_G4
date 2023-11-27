import os,logging
import threading,time
from flask import Flask, request, jsonify
from application.canje_service import CanjeService
from application.ports.productsRepository import ProductsRepository
from infrastructure.adapters.FirebaseProductsRepository import FirebaseProductsRepository
from infrastructure.adapters.postgres_user_query_repository import PostgresUserQueryRepository
from infrastructure.adapters.postgres_user_command_repository import PostgresUserCommandRepository
from infrastructure.adapters.postgres_product_query_repository import PostgresProductQueryRepository
from infrastructure.adapters.postgres_product_command_repository import PostgresProductCommandRepository
from infrastructure.adapters.rabbitmq_consumer import consume_message
from domain.user import User
from application.canjeUseCase import CanjeUseCase
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt
logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING) 

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'test')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 172800 # 2 days
jwt = JWTManager(app)

user_query_repository = PostgresUserQueryRepository()
user_command_repository = PostgresUserCommandRepository()
product_query_repository = PostgresProductQueryRepository()
product_command_repository = PostgresProductCommandRepository()

productRepository = FirebaseProductsRepository()
canjeUseCase = CanjeUseCase(productRepository)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/canjear', methods=['POST'])
@jwt_required()
def canjear():
    active_user_data = get_jwt()
    user = None
    try:
        user = User(active_user_data["id"], active_user_data["points"])
    except:
        return jsonify({"msg": "Invalid token"}), 401

    req_data = request.get_json()
    cart = req_data.get('cart') # Array of indexes of products to buy

    if user is None:
        return jsonify({"msg": "Invalid token"}), 401

    canjeUseCase.canjear(user, cart)
    return jsonify({"msg": "Canje realizado con exito"}), 200

def start_consumer():
    consume_message('canje_queue')

if __name__ == '__main__':
    consumer_thread = threading.Thread(target=start_consumer)
    consumer_thread.start()
    time.sleep(2)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
