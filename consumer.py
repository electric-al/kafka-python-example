# This script connects to Kafka and send a few messages

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "demotopic",
    group_id='my-group',
    auto_offset_reset='earliest',
    bootstrap_servers="127.0.0.1:9092",
)

print('Connected!')

c = 0
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    c += 1
    print ("%d > %s:%d:%d: key=%s value=%s" % (c, message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))