import redis
import time
import os

def start() -> None:
    redis_url = os.environ.get("REDIS_URL") if os.environ.get("REDIS_URL") is not None else "redis://localhost:6379/0"
    conn = redis.Redis.from_url(redis_url)


    start = time.time()
    large_data = bytearray(49152000 * 4)
    large_data[2000] = 5
    conn.set("my_large_data", bytes(large_data))
    print(f"Successfully set \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start) * 1000}ms")
