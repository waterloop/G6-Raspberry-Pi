import time 
import can
bustype = 'socketcan_native'
channel = 'can0'


""""ID: the class of the data we are sending
    This function sends a message over CAN with a specified class as labeled in config.py

"""
def SEND_MESSAGE(message_type):
    # define data object 
    send_data = []
    if message_type.classifer=="BMS_DATA":
        send_data = [message_type.temperature[0], message_type.temperature[1], message_type.temperature[2], message_type.temperature[3],message_type.temperature[4],message_type.temperature[5], error]
    # continue else if chains 
    bus=can.interface.Bus(channel=channel, bustype=bustype)
    msg = can.Message(arbitration_id=message_type.arbitration_id, data=send_data)
    bus.send(msg)
    return True
def RECIEVE_MESSAGE(message_type):
    return True


