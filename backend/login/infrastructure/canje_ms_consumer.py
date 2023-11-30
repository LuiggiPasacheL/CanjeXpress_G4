
import pika, time, logging, json

from application.ports.user_repository import UserRepository

queue_name = 'canje_user_queue'

def callback(ch, method, properties, body):
    # Por ahora, simplemente imprime el mensaje.
    logging.critical(f'Received {body}')

def update_user_points(ch, method, properties, body, userRepository: UserRepository):
    logging.critical(f'Received {body}')
    # Body: 
    # Received b'{"user_id": 1, "user_points": 9800, "products": [{"id": 1, "points": 100, "stock": 100, "requiredQuantity": 1}, {"id": 2, "points": 100, "stock": 100, "requiredQuantity": 1}]}'
    # Se parsea el body a un diccionario
    user_data = json.loads(body)

    # Se obtiene el id del usuario
    user_id = int(user_data['user_id'])

    # Se obtiene la cantidad de puntos que tiene el usuario
    user_points = int(user_data['user_points'])

    userRepository.update_user_points(user_id, user_points)

    # Se obtiene la lista de productos que se canjearon
    products = user_data['products']

    # Se itera sobre la lista de productos canjeados
    for product in products:
        userRepository.update_product_user(user_id, product['id'], product['requiredQuantity'])

def consume_canje_message(userRepository: UserRepository):
    time.sleep(5)
    credentials = pika.PlainCredentials(username='user', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))   
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=
                          lambda ch, method, properties, body: update_user_points(ch, method, properties, body, userRepository), 
                          auto_ack=True)

    channel.start_consuming()

