
import multiprocessing
from multiprocessing import shared_memory
from multiprocessing.synchronize import Event
import time
import threading
def CAN_shmem_listener(shmem_name: str, data_available: Event, data_processed: Event):
    """
    Listens for CAN bus messages, writes them to shared memory.
    """
    shm = shared_memory.SharedMemory(name=shmem_name)
    while True:
        message = b"test message from CAN bus"
        data_processed.wait()
        data_processed.clear()  

        shm.buf[:len(message)] = message
        data_available.set()  

def CAN_shmem_processor(shmem_name: str, data_available: Event, data_processed: Event):
    """
    Processes messages from the CAN bus shared memory.
    """
    shm = shared_memory.SharedMemory(name=shmem_name)
    while True:
        data_available.wait()
        data_available.clear() 

        message_length = len(b"test message from CAN bus")
        message = bytes(shm.buf[:message_length]).decode('utf-8')

        print(f"Processed message: {message}")

        data_processed.set()  


def main():
    shm = shared_memory.SharedMemory(create=True, size=1024)
    ctx = multiprocessing.get_context()

    data_available = ctx.Event()
    data_processed = ctx.Event()
    
    data_processed.set()
    listener_process = multiprocessing.Process(target=CAN_shmem_listener, args=(shm.name, data_available, data_processed))
    processor_process = multiprocessing.Process(target=CAN_shmem_processor, args=(shm.name, data_available, data_processed))
    listener_process.start()
    processor_process.start()

    # Allow processes to run for a while then shut them down for test purposes
    try:
        # Let them run for some time
        listener_process.join(timeout=10)  # Timeout in seconds
        processor_process.join(timeout=10)
    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup: Terminate processes
        listener_process.terminate()
        processor_process.terminate()

        # Close and unlink shared memory
        shm.close()
        shm.unlink()

    return 0


if __name__ == "__main__":
    main()