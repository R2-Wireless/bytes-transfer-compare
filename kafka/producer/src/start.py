import time
import os
import json
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')


def start() -> None:
    print("sleeping...")
    time.sleep(5)
    print("starting!!!")
    kafka_host = os.environ.get("KAFKA_HOST") if os.environ.get("KAFKA_HOST") is not None else "localhost:9092"
    producer = KafkaProducer(
        bootstrap_servers=[kafka_host],
        value_serializer=serializer
    )

    large_data = bytearray(49152000 * 4)
    large_data_bytes = bytes(large_data)
    start = time.time()
    producer.send('my_large_data_stream', large_data_bytes.decode())
    print(f"Successfully set \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start) * 1000}ms")
