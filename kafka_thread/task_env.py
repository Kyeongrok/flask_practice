from confluent_kafka import Consumer

class TaskEnv:
    kafka = None
    def __init__(self):

        self.kafka = KafkaUtil()
        print('init kafka')

class KafkaUtil:

    def get_consumer(self):
        c = Consumer({
        'bootstrap.servers': 'localhost',
        'group.id': 'foo',
        "enable.auto.commit":False,
        'auto.offset.reset': 'earliest'})

        return c

    def __init__(self):
        print('kafka')
        # config map을 {}로 받음
        # receive secret as {}

        self.consumer = self.get_consumer()
        self.produce = None
