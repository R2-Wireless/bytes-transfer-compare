import time

def start() -> None:
    data_file_path = '/shared_data/data.txt'
    large_data = bytearray(49152000 * 4 * 4)
    large_data[2000] = 5
    large_data_bytes = bytes(large_data)
    start = time.time()
    with open(data_file_path, 'wb') as file:
        file.write(large_data_bytes)
    print(f"Successfully write \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start) * 1000}ms")
