# kafka-python-example

Simple example to get started with docker.

To run:

```
docker-compose up -d
pip install -r requirements.txt

In window 1:
python consumer.py
(start more if you wish)

In window 2:
python producer.py

```

## Things to try

Try running the consumer.py again but changing the `group_id`. You should see you see the SAME messages again, as the new consumer group will replay from the `auto_offset_reset=earliest` position. This shows how the messages are persisted in the topic partitions and can be re-read with a new consumer group.

## TODO:

- Advanced partitioning
- Avro examples
- Schema registry
