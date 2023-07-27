import time
import os
import json
from kafka import KafkaConsumer

def serializer(message):
    return json.dumps(message).encode('utf-8')


def start() -> None:
    print("sleeping...")
    time.sleep(5)
    print("starting!!!")
    kafka_host = os.environ.get("KAFKA_HOST") if os.environ.get("KAFKA_HOST") is not None else "localhost:9092"
    consumer = KafkaConsumer(
        'my_large_data_stream',
        bootstrap_servers=kafka_host,
        auto_offset_reset='earliest'
    )
    
    print("start consuming!!!")
    for message in consumer:
        print(f"size data = {len(message.value)}")
