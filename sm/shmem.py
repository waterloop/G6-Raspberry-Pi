# Declaration for shared memory functions

# data_available: EVENT flag that indicates to the processor functions that there is shared memory ready to be written
# data_processed: EVENT flag that indicates that data has been processed. we are ready to write a new message to shmem

from multiprocessing import shared_memory
from multiprocessing.synchronize import Event

def CAN_shmem_listener(shmem_name: str, data_available: Event, data_processed: Event):
    """
    function description
    needs to create the listener thread for the CAN bus process
    
    """
    
    shm = shared_memory.SharedMemory(name=shmem_name)
    while True:
        # read from CAN bus 
        message = b"test" # b is used to cast to byte 
        data_processed.wait()
        data_processed.clear()

        shm.buf[:len(message)] = message
        data_available.set


def CAN_shmem_processor(shmem_name, data_available, data_processed):
    """
    function description
    needs to create the processor thread for the CAN bus shared memory

    """
    shm = shared_memory.SharedMemory(name=shmem_name)
    while True:
        data_available.wait()
        data_available.clear() 

        message_length = len(b"test message from CAN bus")
        message = bytes(shm.buf[:message_length]).decode('utf-8')

        print(f"Processed message: {message}")

        data_processed.set()  


def BT_shmem_listener(shmem_name, data_available, data_processed):
    shm = shared_memory.SharedMemory(name=shmem_name)
    while True:
        # run func to get server shared memory 
        # wait for this func to run
        # that fun needs to load to have a return value
        # RUN THE SERVER GET SHMEM FUNCTION
        # HAVE THE SERVER LOAD THE BT MESSAG TO SHMEM WHNE IT RECIEVES IT
        # FUNCTION RETURNS 
        # THIS FUNCTION RUNS THE REST OF IT'S CODE ( VERY FEW CLOCK CYCLES)
        # RESTARTS THE SERVER SHMEM LISTENER


        # read from server shmem 
        message = b"test" # b is used to cast to byte 
        data_processed.wait()
        data_processed.clear()

        shm.buf[:len(message)] = message
        data_available.set    


def BT_shmem_processor(shmem_name, data_available, data_processed): 
    return 0
