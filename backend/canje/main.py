import os,logging
import threading,time
from flask import Flask, request, jsonify
from application.canje_service import CanjeService
from infrastructure.adapters.postgres_user_query_repository import PostgresUserQueryRepository
from infrastructure.adapters.postgres_user_command_repository import PostgresUserCommandRepository
from infrastructure.adapters.postgres_product_query_repository import PostgresProductQueryRepository
from infrastructure.adapters.postgres_product_command_repository import PostgresProductCommandRepository
from infrastructure.adapters.rabbitmq_consumer import consume_message
from flask_cors import CORS
logging.basicConfig(level=logging.INFO)
logging.getLogger("pika").setLevel(logging.WARNING) 
app = Flask(__name__)
CORS(app)

user_query_repository = PostgresUserQueryRepository()
user_command_repository = PostgresUserCommandRepository()
product_query_repository = PostgresProductQueryRepository()
product_command_repository = PostgresProductCommandRepository()

canje_service = CanjeService(user_query_repository, user_command_repository, product_query_repository, product_command_repository)

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

def start_consumer():
    consume_message('canje_queue')

if __name__ == '__main__':
    consumer_thread = threading.Thread(target=start_consumer)
    consumer_thread.start()
    time.sleep(2)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
