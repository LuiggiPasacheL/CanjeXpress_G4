
import pika,time,logging

def callback(ch, method, properties, body):
    # Por ahora, simplemente imprime el mensaje.

    logging.critical(f'''\n\n\n##################\n\n\n [x] Received {body}\n\n\n##################\n\n\n''')


def consume_message(queue_name):
    time.sleep(5)
    credentials = pika.PlainCredentials(username='user', password='password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))   
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
