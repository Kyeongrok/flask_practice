from confluent_kafka import Consumer
import time

consumer_group_id = 'foo'
consumer = Consumer({
    'bootstrap.servers': 'localhost',
    'group.id': consumer_group_id,
    "enable.auto.commit":False,
    'auto.offset.reset': 'earliest'})

topic_name = 'adc-100'
consumer.subscribe([topic_name])

while True:
    msg = consumer.poll(timeout=1.0)
    if msg != None:
        print(msg.value())
    else:
        print('Msg is none.')

    time.sleep(0.1)