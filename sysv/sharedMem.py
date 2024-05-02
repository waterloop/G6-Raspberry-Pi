import sysv_ipc

shm = sysv_ipc.SharedMemory(777)
if shm:
    s = shm.read()
    s = s.decode()
    i = s.find('\0')
    if i != -1:
        s = s[:i]
    print(s)