#include <iostream>
#include <cstring>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include "shmem.h"

void shmem_BT_worker(const char* name, const char* message){
    // shmem.cpp skeleton to take BT message and put it to python process
    const int SIZE = 4096;
    //const char* name = "MySharedMemory";

    int shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    ftruncate(shm_fd, SIZE);
    int protection = PROT_READ | PROT_WRITE;
    void* ptr = mmap(0, SIZE, protection, MAP_SHARED, shm_fd, 0);

    //const char* message = "Hello from C++!\nMy name is Xander!\n"; // this is our message
    sprintf((char*)ptr, "%s", message);

    std::cout << "Message written to shared memory: " << message << std::endl;

    std::cout << "Press ENTER to exit..." << std::endl;
    std::cin.get();


    munmap(ptr, SIZE);
    close(shm_fd);
    shm_unlink(name);
}

// int main() {
//     // shmem.cpp skeleton to take BT message and put it to python process
//     const int SIZE = 4096;
//     const char* name = "MySharedMemory";

//     int shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);
//     ftruncate(shm_fd, SIZE);
//     int protection = PROT_READ | PROT_WRITE;
//     void* ptr = mmap(0, SIZE, protection, MAP_SHARED, shm_fd, 0);

//     const char* message = "Hello from C++!\nMy name is Xander!\n"; // this is our message
//     sprintf((char*)ptr, "%s", message);

//     std::cout << "Message written to shared memory: " << message << std::endl;

//     std::cout << "Press ENTER to exit..." << std::endl;
//     std::cin.get();


//     munmap(ptr, SIZE);
//     close(shm_fd);
//     shm_unlink(name);

//     return 0;
// }
