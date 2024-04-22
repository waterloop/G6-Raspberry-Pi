import time 
import can
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
    if message_type.can_id == BMS_DATA.can_id:
        send_data = [message_type.temperature[0], 
                    message_type.temperature[1], 
                    message_type.temperature[2], 
                    message_type.temperature[3],
                    message_type.temperature[4],
                    message_type.temperature[5],
                    message_type.error_code]

    elif message_type.can_id == SENSORS_BOARD_DATA.can_id:
        send_data = [message_type.temperature[0],
                    message_type.temperature[1],
                    message_type.imu_data,
                    message_type.pressure_sensor_data,
                    message_type.error_code]
        
    elif message_type.can_id == MOTOR_CONTROLLER_DATA.can_id:
        send_data = [message_type.battery_voltage,
                    message_type.battery_current,
                    message_type.motor_speed,
                    message_type.motor_controller_temp,
                    message_type.driving_direction,
                    message_type.error_code]

    elif message_type.can_id == KELLY_DATA_FRAME1.can_id:
        send_data = [message_type.driving_direction_kelly,
                    message_type.motor_speed_kelly,
                    message_type.motor_error_code_kelly]

    elif message_type.can_id == KELLY_DATA_FRAME2.can_id:
        send_data = [message_type.battery_voltage_kelly,
                    message_type.battery_current_kelly,
                    message_type.motor_temp_kelly,
                    message_type.motor_controller_temp_kelly]

    else:
        send_data = []

    bus=can.interface.Bus(channel=channel, bustype=bustype)
    msg = can.Message(arbitration_id=message_type.arbitration_id, data=send_data)
    bus.send(msg)
    return True
def RECIEVE_MESSAGE(message_type):
    return True

