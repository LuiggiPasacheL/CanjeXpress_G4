import pika
import json

from application.ports.userRepository import UserRepository
from domain.product import Product
from domain.user import User

class PikaUserRepository(UserRepository):
    
    def __init__(self):
        self.queue_name = 'canje_user_queue'
        self.credentials = pika.PlainCredentials(username='user', password='password')

    def updateUser(self, updated_user: User, products: list[Product]):
        """Updates user points and products reedemed by user"""
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=self.credentials))   
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)

        message = {
            'user_id': updated_user.id,
            'user_points': updated_user.points,
            'products': [product.to_dict() for product in products],
        }
        channel.basic_publish(exchange='',
                      routing_key=self.queue_name,
                      body=json.dumps(message),
                      properties=pika.BasicProperties(delivery_mode = 2,)
        )
        connection.close()
