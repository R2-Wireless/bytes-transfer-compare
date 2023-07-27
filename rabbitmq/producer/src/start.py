import time
import pika


def start() -> None:
    print("sleeping...")
    time.sleep(5)
    print("starting!!!")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    large_data = bytearray(49152000 * 4)
    large_data[2000] = 5
    large_data_bytes = bytes(large_data)

    start = time.time()
    channel.queue_declare(queue="my_large_data")

    channel.basic_publish(exchange='', routing_key='my_large_data', body=large_data_bytes)

    print(f"Successfully publish \"my_large_data\" of size {len(large_data_bytes)}, that took {(time.time() - start) * 1000}ms")
    connection.close()
