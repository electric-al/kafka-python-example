# This script connects to Kafka and send a few messages

from kafka import KafkaProducer
import json
import random

producer = KafkaProducer(
    bootstrap_servers="127.0.0.1:9092",
    linger_ms=500 # Max batching time
)

x = random.randint(1,100)

for i in range(1, 10000):
    msg = {'key':i,'a':x}
    js = json.dumps(msg)
    print("Sending: {}".format(js))
    producer.send("demotopic", js.encode("utf-8"))

# Force sending of all messages
producer.flush()