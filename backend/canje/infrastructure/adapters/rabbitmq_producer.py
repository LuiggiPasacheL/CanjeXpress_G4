
import pika,time

def publish_message(queue_name, message_body):
    time.sleep(5)
    credentials = pika.PlainCredentials(username='user', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))   
    channel = connection.channel()
    
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message_body)
    
    connection.close()
