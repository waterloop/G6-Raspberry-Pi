import bluetooth

def setup_bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    server_sock.bind(("", port))
    server_sock.listen(1)

    bluetooth.advertise_service(server_sock, "RaspberryPiService",
                                service_id="00001101-0000-1000-8000-00805F9B34FB",
                                service_classes=[bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])

    print("Waiting for connection on RFCOMM channel %d" % port)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            received_command = data.decode("utf-8").strip()
            print("Received:", received_command)
            
            # Respond to the command "HELLO"
            if received_command == "HELLO":
                client_sock.send("HI")
            else:
                client_sock.send("Unknown Command")
    except IOError:
        pass
    finally:
        client_sock.close()
        server_sock.close()

setup_bluetooth_server()