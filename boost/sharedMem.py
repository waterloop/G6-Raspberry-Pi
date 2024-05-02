import mmap

if __name__ == "__main__":
    with open("myshm", "r+b") as f:
        shm_a = mmap.mmap(f.fileno(), 0)
        print(shm_a.readline())
        print(shm_a[0:4])
        shm_a.close()