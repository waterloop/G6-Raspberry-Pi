import time 
import can
from ctypes import  c_uint8, c_uint16, c_uint32
import struct
from config import *

#instantiate objects of all classes
global_vars = GLOBAL()
bms_data = BMS_DATA()
sensors_board_data = SENSORS_BOARD_DATA()
motor_controller_data = MOTOR_CONTROLLER_DATA()
kelly_data_frame1 = KELLY_DATA_FRAME1()
kelly_data_frame2 = KELLY_DATA_FRAME2()

#assign CAN_IDs to all instantiated objects
bms_data.can_id = global_vars.BMS_BOARD
sensors_board_data.can_id = global_vars.SENSOR_BOARD
motor_controller_data.can_id = global_vars.MOTOR_CONTROLLER: #CHECK this might be wrong
kelly_data_frame1.can_id = global_vars.MOTOR_CONTROLLER_1
kelly_data_frame2.can_id = global_vars.MOTOR_CONTROLLER_2

#define send and receive functions
"""
FUNCTION:       RECEIVE_MESSAGE
@ARG can_bus:   passed can object
RETURN:         none
WHAT IT DO?     receives a message on the bus. Writes message data to the correct
                instantiated object based on the message's arbitration ID
"""
def RECEIVE_MESSAGE(can_bus):
    rx_msg = can_bus.Message
    print(rx_msg)

    if rx_msg.arbitration_id == global_vars.BMS_BOARD:
        

"""
FUNCTION:       CREATE_SEND_DATA
@ARG can_bus:   
RETURN:         data packet. Bytearray.
WHAT IT DO?     Creates 'data' based on the arbitrationID 
                of the frame we wish to send. Reveals the current state of 
                the instantiated objects.
"""
def CREATE_SEND_DATA(arbitrationID):
    # define data object 
    data = []
    if arbitrationID == global_vars.BMS_BOARD:
        data = [bms_data.temperature[0], 
                bms_data.temperature[1], 
                bms_data.temperature[2], 
                bms_data.temperature[3],
                bms_data.temperature[4],
                bms_data.temperature[5],
                bms_data.error_code,
                0]

    elif arbitrationID == global_vars.SENSOR_BOARD:
        data = [sensors_board_data.temperature[0],
                sensors_board_data.temperature[1],
                sensors_board_data.imu_data,
                sensors_board_data.pressure_sensor_data,
                sensors_board_data.error_code,
                0,
                0,
                0]
        
    elif arbitrationID == global_vars.MOTOR_CONTROLLER: #CHECK this might be wrong
        data = [motor_controller_data.battery_voltage,
                motor_controller_data.battery_current,
                motor_controller_data.motor_speed,
                motor_controller_data.motor_controller_temp,
                motor_controller_data.driving_direction,
                motor_controller_data.error_code,
                0,
                0]

    elif arbitrationID == global_vars.MOTOR_CONTROLLER_1:
        data = [kelly_data_frame1.driving_direction_kelly,
                kelly_data_frame1.motor_speed_kelly,
                kelly_data_frame1.motor_error_code_kelly,
                0,
                0,
                0,
                0]

    elif arbitrationID == global_vars.MOTOR_CONTROLLER_2:
        data = [kelly_data_frame2.battery_voltage_kelly,
                kelly_data_frame2.battery_current_kelly,
                kelly_data_frame2.motor_temp_kelly,
                kelly_data_frame2.motor_controller_temp_kelly,
                0,
                0,
                0,
                0]

    else:
        data = [0, 0, 0, 0, 0, 0, 0, 0]

    return data


