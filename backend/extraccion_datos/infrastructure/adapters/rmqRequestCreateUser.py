
import pika
import json

from application.ports.requestCreateUser import RequestCreateUser

class RMQRequestCreateUser(RequestCreateUser):

    def __init__(self):
        self.queue_name = 'create_user_request'
        self.credentials = pika.PlainCredentials(username='user', password='password')

    def sendMessage(self, users: list[dict]):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', credentials=self.credentials)
        )
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)
        channel.basic_publish(exchange='',
                      routing_key=self.queue_name,
                      body=json.dumps(users),
                      properties=pika.BasicProperties(delivery_mode = 2,)
        )
        connection.close()
