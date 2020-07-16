# kafka-python-example

Simple example to get started with docker.

To run:

```
documer-compose -d up
pip install -r requirements.txt

In window 1:
python consumer.py
(start more if you wish)

In window 2:
python producer.py

```

## Things to try

Try running the consumer.py again but changing the `group_id`. You should see you see the SAME messages again, as the new consumer group will replay from the `auto_offset_reset=earliest` position.

## TODO:

- Advanced partitioning
- Avro examples
- Schema registry
