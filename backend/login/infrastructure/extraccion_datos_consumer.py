
import pika, time, logging, json, bcrypt

from application.ports.user_repository import UserRepository

queue_name = 'create_user_request'

def register_user(ch, method, properties, body, userRepository: UserRepository):
    users_data = json.loads(body)

    logging.info(f'Received {len(users_data)} users')

    # Bycrypt passwords from users_data array
    if len(users_data) > 0:
        for user_data in users_data:
            user_data['password'] = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        userRepository.bulk_create_users(users_data)


def consume_extraccion_datos_message(userRepository: UserRepository):
    time.sleep(5)
    credentials = pika.PlainCredentials(username='user', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))   
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=
                          lambda ch, method, properties, body: register_user(ch, method, properties, body, userRepository), 
                          auto_ack=True)

    channel.start_consuming()

