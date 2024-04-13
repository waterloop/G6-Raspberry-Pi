import time 
import can
import config
from ctypes import  c_uint8, c_uint16, c_uint32
import struct
from config import GLOBAL, BMS_DATA, SENSORS_BOARD_DATA, MOTOR_CONTROLLER_DATA, KELLY_DATA_FRAME1, KELLY_DATA_FRAME2
# struct justification
# Python interpreter will sometimes add padding. we need to serialize into a string of bytes and then send to network

bustype = 'socketcan_native'
channel = 'can0'

""""ID: the class of the data we are sending
    This function sends a message over CAN with a specified class as labeled in config.py
"""

def SEND_MESSAGE(message_type):
    # define data object 
    send_data = []
    if message_type.classifer=="BMS_DATA":
        send_data = [message_type.temperature[0], message_type.temperature[1], message_type.temperature[2], message_type.temperature[3],message_type.temperature[4],message_type.temperature[5], message_type.error_code]

    # continue else-if chain
    bus=can.interface.Bus(channel=channel, bustype=bustype)
    msg = can.Message(arbitration_id=message_type.arbitration_id, data=send_data)
    bus.send(msg)
    return True
def RECIEVE_MESSAGE(message_type):
    return True

