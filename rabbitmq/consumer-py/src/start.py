import time
import pika

def callback_func(channel, method, properties, body):
    assert(body[2000] == 5)
    print(f"Successfully Got \"my_large_data\" of size {len(body)}")


def start() -> None:
    print("sleeping...")
    time.sleep(5)
    print("starting!!!")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue="my_large_data")
    channel.basic_consume(
        queue="my_large_data", on_message_callback=callback_func, auto_ack=True)

    print("start consuming...")
    channel.start_consuming()

    
