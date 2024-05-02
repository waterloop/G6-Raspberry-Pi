### Intro

This is an implementation of shared memory between `.cpp` and `.py` processes using the `boost/interprocesses` library to create the shared memory in `.cpp` and then using the `mem` library to read from the shared memory in `.py`. 

This example aims to write values to the shared memory in the `.cpp` process and then read the values in the `.py` process and print it out.

The `.py` code is NOT tested and so may not work but aligns very closely with the documentation of the `mem` library (given below in resources).


### Resources
[StackOverFlow Post on installing Boost on Ubunutu](https://stackoverflow.com/questions/12578499/how-to-install-boost-on-ubuntu)
[Building Boost Guide](https://anycoder.wordpress.com/2014/04/28/building-boost/)
[SourceForge Boost Instaler](https://anycoder.wordpress.com/2014/04/28/building-boost/)
[Python `mmap` Library Documentation](https://docs.python.org/3/library/mmap.html)