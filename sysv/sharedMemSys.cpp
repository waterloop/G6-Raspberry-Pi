#include <iostream>
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>

// Create the shared memory
shmid = shmget(777, 512 * 8, IPC_CREAT | 0666)
// Attach the memory.
shared_memory = (char*) shmat(shmid, NULL, 0)
// Create pointer to shared memory
fptr = reinterpret_cast<float *>(shared_memory);
// Output contents of shared memory
for (int i = 0; i < 63; i += 3)
{
    std::cout << fptr[i] << " " << fptr[i + 1] << " " << fptr[i + 2] << "\n";
}