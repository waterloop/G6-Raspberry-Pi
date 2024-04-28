# Declaration for shared memory functions
from multiprocessing import shared_memory, Event

def CAN_shmem_listener(shmem_name, data_available, data_processed):
    return 0


def CAN_shmem_processor(shmem_name, data_available, data_processed):
    return 0


def BT_shmem_listener(shmem_name, data_available, data_processed):
    return 0
