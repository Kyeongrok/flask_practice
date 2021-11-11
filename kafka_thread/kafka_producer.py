from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost'})

for i in range(10):
    print(i)
    p.produce('adc-100', f'hello{i}', 'world')
    p.flush()
