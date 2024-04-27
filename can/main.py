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
	    CAN1 = can.interface.Bus(channel='can0', bustype='socketcan')   #instance CAN object
    except OSError:
	    print('Cannot find PiCAN board.')
	    exit()
    print('Ready')   

    #create listener and notifier             
    #(TODO: configure CAN connection (masks, etc))
    CAN1_listener = msg_rx_routine                                         
    CAN1_notifier = can.Notifier(CAN1, [CAN1_listener])      #assign listener to notifier


if __name__ == "__main__":
    main()