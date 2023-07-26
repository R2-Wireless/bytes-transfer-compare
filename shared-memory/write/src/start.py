from multiprocessing import shared_memory
import time
import array

def start() -> None:
    start = time.time()
    shm = shared_memory.SharedMemory(create=True, name="my_large_data", size=49152000 * 4)
    shm.buf[2000] = 6 # Modify single byte at a time
    print(f"Successfully write \"my_large_data\" of size {len(shm.buf)}, that took {(time.time() - start) * 1000}ms")
    time.sleep(100)
    shm.close()
    shm.unlink() # Call unlink only once to release the shared memory

# def read() -> None:
#     start = time.time()
#     shm = shared_memory.SharedMemory("my_large_data")
#     assert(shm.buf[2000] == 6)
#     print(f"Successfully read \"my_large_data\" of size {len(shm.buf)}, that took {(time.time() - start) * 1000}ms")
#     shm.close()
