
"""
tight poll the server.cpp shmem buffer
read then return 0=
this will be a child process, spawned 
"""
import mmap
import os

# Name of the shared memory segment
name = 'MySharedMemory'

# Ensure C++ program has started and created the shared memory
input("Press Enter after the C++ program has started...")

try:
    # Open the shared memory object
    shm_fd = os.open(f'/dev/shm/{name}', os.O_RDONLY)

    # Memory map the file descriptor
    with mmap.mmap(shm_fd, 4096, access=mmap.ACCESS_READ) as m:
        # Read the content from shared memory
        null_byte_index = m.find(b'\x00')
        if null_byte_index != -1:
            print("String read from shared memory:", m[:null_byte_index].decode())
        else:
            print("String read from shared memory:", m.read(4096).decode())

    os.close(shm_fd)
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Make sure the C++ shared memory segment 'MySharedMemory' is created and available.")
except Exception as e:
    print(f"An error occurred: {e}")

