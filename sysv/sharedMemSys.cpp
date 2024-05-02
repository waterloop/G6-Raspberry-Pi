#include <iostream>
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>

// Create the shared memory
shmid = shmget(777, 512 * 8, IPC_CREAT | 0666)
// Attach the memory.
shared_memory = shmat(shmid, NULL, 0)

char s[1024]{'Hi! This is me writing a string to the shared memory!'};
std::strcpy((char*)shared_memory, s);

//Output contents of shared memory
for (int i = 0; i < 63; i += 3)
{
    std::cout << (char*)shared_memory[i] << " " << (char*)shared_memory[i + 1] << " " << (char*)shared_memory[i + 2] << "\n";
}