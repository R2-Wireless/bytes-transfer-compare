from multiprocessing import shared_memory
import time
import mmap

def start() -> None:
    # size = 49152000 * 4
    # shm = shared_memory.SharedMemory(create=True, name="my_large_data", size=size)
    # large_data = bytearray(size)
    # large_data[2000] = 5
    # start = time.time()
    # shm.buf[:] = large_data # Modify all data
    # print(f"Successfully write \"my_large_data\" of size {len(shm.buf)}, that took {(time.time() - start) * 1000}ms")
    # time.sleep(100)
    # shm.close()
    # shm.unlink() # Call unlink only once to release the shared memory
    data = b"Hello, this is shared memory data!"
    file_path = "shared_memory.bin"

    # Create a writable shared memory file and write the data
    with open(file_path, "wb") as f:
        f.write(b"bla vla bla")  # Ensure the file has the required size
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as shared_memory:
            shared_memory.write(data)
