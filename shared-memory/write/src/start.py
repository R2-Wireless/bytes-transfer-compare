import time
import mmap

def start() -> None:
    file_path = "/shared_data/test.mmap"
    size = 49152000 * 4
    large_data = bytearray(size)
    large_data[2000] = 5
    f = open(file_path, "wb")
    f.write(size*b'\0')
    f.close()
    # Create a writable shared memory file and write the data
    with open(file_path, mode="r+b") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            start = time.time()
            mmap_obj.write(large_data)
    print(f"Successfully write \"my_large_data\" of size {len(large_data)}, that took {(time.time() - start) * 1000}ms")
