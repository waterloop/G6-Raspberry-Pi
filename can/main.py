import can
import time
import os
from config import *
from driver import *

def main():

    #CANBUS init
    os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")   #bring up can0 interface at 500kbps
    time.sleep(0.05)
    try:
	    CAN1 = can.interface.Bus(channel='can0', bustype='socketcan')   #instantiate CAN object
    except OSError:
	    print('Cannot find PiCAN board.')
	    exit()
    print('Ready')   

    #create listener and notifier             
    #(TODO: configure CAN connection (masks, etc))
    CAN1_listener = RECEIVE_MESSAGE                                         
    CAN1_notifier = can.Notifier(CAN1, [CAN1_listener])   #assign listener to notifier

    #send and receive messages
    # 1. send
    msg_data = CREATE_SEND_DATA(0)
    msg = can.Message(arbitration_id = 0x57, data = msg_data)
    CAN1.send(msg)

if __name__ == "__main__":
    main()