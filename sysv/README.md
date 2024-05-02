### Intro

This is an implementation of shared memory between `.cpp` and `.py` processes using the `sys/ipc.h` library to create the shared memory in `.cpp` and then using the `sysv_ipc` library to write to the shared memory in `.py`. 

We desire the usecase of writing to the shared memory in `.cpp` and then reading the values with the `.py` process. The following repo gives an excellent example of how to write and read to shared memory using both `.cpp` (`.c` particularly) and `.py`: [Github Demo](https://github.com/mruffalo/sysv_ipc/tree/master/demo).


### Resources
[StackOverFlow Post on sample code](https://github.com/mruffalo/sysv_ipc/tree/master/demo)
[Geeks for Geeks Sample Code](https://www.geeksforgeeks.org/ipc-shared-memory/)
[Sysv_ipc Github Demo Code](https://github.com/mruffalo/sysv_ipc/tree/master/demo/)
[Python `sysv_icp` PyPi Install](https://pypi.org/project/sysv-ipc/)