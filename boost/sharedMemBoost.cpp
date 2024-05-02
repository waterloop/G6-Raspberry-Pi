#include <boost/interprocess/shared_memory_object.hpp>
#include <boost/interprocess/mapped_region.hpp>

int main(int argc, char* argv[])
{
    using namespace boost::interprocess;

    //Remove shared memory on construction and destruction
    struct shm_remove
    {
        shm_remove() { shared_memory_object::remove("myshm"); }
        ~shm_remove() { shared_memory_object::remove("myshm"); }
    } remover;

    //Create a shared memory object.
    shared_memory_object shm(create_only, "myshm", read_write);

    //Set size
    shm.truncate(1000);

    //Map the whole shared memory in this process
    mapped_region region(shm, read_write);

    //Write all the memory to 1
    std::memset(region.get_address(), 1, region.get_size());

    std::system("pause");
}