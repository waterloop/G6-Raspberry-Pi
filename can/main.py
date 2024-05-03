# import can
# import time
# import os
# from config import *
# from driver import RECEIVE_MESSAGE, CREATE_SEND_DATA 

# def main():

#     #CANBUS init
#     os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")   #bring up can0 interface at 500kbps
#     time.sleep(0.05)
#     try:
# 	    CAN0 = can.interface.Bus(channel='can0', bustype='socketcan')   #instantiate CAN object
#     except OSError:
# 	    print('Cannot find PiCAN board.')
# 	    exit()
#     print('Ready')   

#     #create listener and notifier             
#     #(TODO: configure CAN connection (masks, etc))
#     CAN0_listener = RECEIVE_MESSAGE                                        
#     CAN0_notifier = can.Notifier(CAN0, [CAN0_listener])   #assign listener to notifier

#     #send and receive messages
#     # 1. send
#     msg_data = [0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xF0]
#     msg = can.Message(arbitration_id = 0x57, data = msg_data)
#     CAN0.send(msg)
#     os.system("sudo ip link set can0 down")

# if __name__ == "__main__":
#     main()


import can
import time
import os
from config import *
class MessageListener(can.Listener):
    def on_message_received(self, msg):
        print(f'Received message: {msg}')

def main():
    os.system("sudo ip link set can0 up type can bitrate 500000")  # Bring up can0 interface at 500kbps
    #os.system("sudo ip link set can1 up type can bitrate 500000")
    time.sleep(0.05)
    try:
        CAN0 = can.interface.Bus(channel='can0', bustype='socketcan', loopback = True)  # Instantiate CAN object
    except OSError:
        print('Cannot find PiCAN board.')
        exit()
    print('Ready')

    CAN0_listener = MessageListener()
    CAN0_notifier = can.Notifier(CAN0, [CAN0_listener])  # Assign listener to notifier

    msg_data = [(0xF0), (0xF0), (0xF0), (0xF0)]
    msg = can.Message(arbitration_id = 0x57, data = msg_data, is_extended_id = False)
    print(f"MESSAGE: {msg} \n")
    CAN0.send(msg)
    time.sleep(0.001)  # Allow some time for message handling

    CAN0_notifier.stop()
    CAN0.shutdown()

    os.system("sudo ip link set can0 down")
    os.system("sudo ip link set can1 down")

if __name__ == "__main__":
    main()