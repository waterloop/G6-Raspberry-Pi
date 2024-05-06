#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>
#include "shmem.h"
// purpose: receive message from rpi
int main()
{
    struct sockaddr_rc addr = { 0 };
    char BT_address[18] = "34:FE:77:9D:C1:95";
    char response_buffer[1024] = { 0 };

    int s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);

    addr.rc_family = AF_BLUETOOTH;
    addr.rc_channel = (uint8_t) 1;
    str2ba(BT_address, &addr.rc_bdaddr);
    bind(s, (struct sockaddr *)&addr, sizeof(addr)); // bind socket to bluetooth addr

    listen(s, 1);
    socklen_t len = sizeof(addr);

    while (true) { // basically we do a while true loop, if message (from bluetooth) is not null we run the code (shmem)
        int client = accept(s, (struct sockaddr *)&addr, &len);

        ba2str(&addr.rc_bdaddr, response_buffer);
        std::cout << "accepted communication from " << response_buffer << std::endl;
        memset(response_buffer, 0, sizeof(response_buffer));

        // read data from the client
        int bytes_read = read(client, response_buffer, sizeof(response_buffer));
        if(bytes_read > 0) {
            // run shmem.cpp code here
            shmem_BT_worker("BTshmem", response_buffer);
        }

        close(client);
    }

    close(s);
    return 0;
}