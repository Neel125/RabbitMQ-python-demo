import pika
import json

credentials = pika.PlainCredentials("admin", "FNP2@2")
parameters = pika.ConnectionParameters("20.120.37.220", 5672, credentials=credentials)
# myparameters = pika.URLParameters('http://admin:FNP2%402@20.120.37.220:15672/#/')
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()
data = {
    "test": "123",
    "abc": "xyz"
}
for i in range(100000):
    data["counter"] = i
    channel.basic_publish(exchange="FNP_exchange", routing_key="fnp-test",
                          body=bytes(json.dumps(data), encoding="utf-8"))
print("[x] Message sent to consumer")
connection.close()
