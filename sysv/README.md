### Intro

This is an implementation of shared memory between `.cpp` and `.py` processes using the `sys/ipc.h` library to create the shared memory in `.cpp` and then using the `sysv_ipc` library to write to the shared memory in `.py`. 

This example aims to write values to the shared memory in the `.cpp` process and then read the values in the `.py` process and print it out.

The `.py` code is NOT tested and so may not work but aligns very closely with the documentation of the `mem` library (given below in resources).


### Resources
[StackOverFlow Post on sample code](https://github.com/mruffalo/sysv_ipc/tree/master/demo)
[Geeks for Geeks Sample Code](https://www.geeksforgeeks.org/ipc-shared-memory/)
[Sysv_ipc Github Demo Code](https://github.com/mruffalo/sysv_ipc/tree/master/demo/)
[Second Github Sample for sysv_ipc](https://github.com/ajaygunalan/IPC_SHM/tree/master)
[Third Github Sample for sysv_ipc](https://github.com/dovanhuong/ipc_shared_memory_cpp_and_python/blob/main/shared_mem.cpp)
[Python `sysv_icp` PyPi Install](https://pypi.org/project/sysv-ipc/)