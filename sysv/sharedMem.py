import sysv_ipc

shm = sysv_ipc.SharedMemory(777)
if shm:
    offset = 0
    for idx in range(0, 21):
        shm.write(1, offset)
        offset += 4
        shm.write(2, offset)
        offset += 4
        shm.write(3, offset)
        offset += 4