
import pika

def callback(ch, method, properties, body):
    # Por ahora, simplemente imprime el mensaje.
    print(f" [x] Received {body}")

def consume_message(queue_name):
    credentials = pika.PlainCredentials(username='user', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))   
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
