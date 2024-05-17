
"""
tight poll the server.cpp shmem buffer
read then return 0=
this will be a child process, spawned 
"""
import os
import mmap


"""REMOVE MAIN IN PROD""" 
def main():
    s = server_cpp_to_py()


def server_cpp_to_py():
    name = 'BTshmem'
  #  input("Press Enter after the C++ program has started...")
    message = ""

    try:
        shm_fd = os.open(f'/dev/shm/{name}', os.O_RDONLY)
        
        try:
            with mmap.mmap(shm_fd, 4096, access=mmap.ACCESS_READ) as m:
                null_byte_index = m.find(b'\x00')
                if null_byte_index != -1:
                    message = m[:null_byte_index].decode()
                else:
                    message = m.read(4096).decode()

            print("String read from shared memory:", message)
        
        finally:
            os.close(shm_fd)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Make sure the C++ shared memory segment 'BTshmem' is created and available.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return message

if __name__ == "__main__":
    main()
