import pika
import queue
import json
import time


credentials = pika.PlainCredentials("admin", "FNP2@2")
parameters = pika.ConnectionParameters("20.120.37.220", 5672, credentials=credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()


def callback(ch, method, properties, body):
    print(f'{body} is received')


# channel.basic_consume(queue="FNP_queue", on_message_callback=callback, auto_ack=True)
# channel.start_consuming()
for method, properties, body in channel.consume("FNP_queue"):
    st = time.time()
    print(body)
    channel.basic_ack(method.delivery_tag)
    print("end", time.time() - st)
    break
