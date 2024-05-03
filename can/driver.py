import time 
import can
from ctypes import  c_uint8, c_uint16, c_uint32
import struct
from config import *

#instantiate objects of all classes
global_vars = GLOBAL()
bms_data = BMS_DATA()
sensors_1 = SENSORS_1()
sensors_2 = SENSORS_2()
motor_controller_data = MOTOR_CONTROLLER_DATA()

#assign CAN_IDs to all instantiated objects
bms_data.can_id = global_vars.BMS_BOARD
sensors_1.can_id = global_vars.SENSOR_BOARD_1
sensors_2.can_id = global_vars.SENSOR_BOARD_2
motor_controller_data.can_id = global_vars.MOTOR_CONTROLLER

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

    rx_data = rx_msg.data

    if (rx_msg.arbitration_id == global_vars.BMS_BOARD) or (rx_msg.arbitration_id == global_vars.BMS_BOARD_WARN):
        bms_data.temperature[0]=rx_data[0]
        bms_data.temperature[1]=rx_data[1]
        bms_data.temperature[2]=rx_data[2]
        bms_data.temperature[3]=rx_data[3]
        bms_data.temperature[4]=rx_data[4]
        bms_data.temperature[5]=rx_data[5]
        bms_data.error_code = rx_data[6]
    
    elif (rx_msg.arbitration_id == global_vars.SENSOR_BOARD_1) or (rx_msg.arbitration_id == global_vars.SENSOR_BOARD_1_WARN):
        sensors_board_data.temperature[0] = rx_data[0]
        sensors_board_data.temperature[1] = rx_data[1]
        sensors_board_data.imu_data = rx_data[2]
        sensors_board_data.pressure_sensor_data = rx_data[3]
        sensors_board_data.error_code = rx_data[4]
    
    elif (rx_msg.arbitration_id == global_vars.SENSOR_BOARD_2) or (rx_msg.arbitration_id == global_vars.SENSOR_BOARD_2_WARN):
        sensors_board_data.temperature[0] = rx_data[0]
        sensors_board_data.temperature[1] = rx_data[1]
        sensors_board_data.imu_data = rx_data[2]
        sensors_board_data.pressure_sensor_data = rx_data[3]
        sensors_board_data.error_code = rx_data[4]

    elif rx_msg.arbitration_id == global_vars.MOTOR_CONTROLLER:
        motor_controller_data.battery_voltage = rx_data[0]
        motor_controller_data.battery_current = rx_data[1]
        motor_controller_data.motor_speed = rx_data[2]
        motor_controller_data.motor_controller_temp = rx_data[3]
        motor_controller_data.driving_direction = rx_data[4]
        motor_controller_data.error_code = rx_data[5]
    
"""
FUNCTION:       CREATE_SEND_DATA
@ARG arbitration_id
RETURN:         data packet. Bytearray.
WHAT IT DO?     Creates 'data' based on the arbitrationID 
                of the frame we wish to send. Reveals the current state of 
                the instantiated objects.
"""
def CREATE_SEND_DATA(arbitrationID):
    # define data object 
    data = []
    if (arbitrationID == global_vars.BMS_BOARD) or (arbitrationID == global_vars.BMS_BOARD_WARN):
        data = [bms_data.temperature[0], 
                bms_data.temperature[1], 
                bms_data.temperature[2], 
                bms_data.temperature[3],
                bms_data.temperature[4],
                bms_data.temperature[5],
                bms_data.error_code,
                0]

    elif (arbitrationID == global_vars.SENSOR_BOARD_1) or (arbitrationID == global_vars.SENSOR_BOARD_1_WARN):

        msb_pressure = bytes(sensors_1.pressure_sensor_data & (0b11111111 << 8))
        lsb_pressure = bytes(sensors_1.pressure_sensor_data & 0b11111111)
        msb_lim_temp_0 = bytes(sensors_1.lim_temperature[0] & (0b11111111 << 8))
        lsb_lim_temp_0 = bytes(sensors_1.lim_temperature[0] & (0b11111111))
        msb_lim_temp_1 = bytes(sensors_1.lim_temperature[1] & (0b11111111 << 8))
        lsb_lim_temp_1 = bytes(sensors_1.lim_temperature[1] & (0b11111111))

        data = [msb_pressure,
                lsb_pressure,
                msb_lim_temp_0,
                lsb_lim_temp_0,
                msb_lim_temp_1,
                lsb_lim_temp_1,
                sensors_1.error_code,
                0]

    elif (arbitrationID == global_vars.SENSOR_BOARD_2) or (arbitrationID == global_vars.SENSOR_BOARD_2_WARN):

        msb_x_accel = bytes(sensors_2.x_acceleration & (0b11111111 << 8))
        lsb_x_accel = bytes(sensors_2.x_acceleration & (0b11111111))
        msb_y_accel = bytes(sensors_2.y_acceleration & (0b11111111 << 8))
        lsb_y_accel = bytes(sensors_2.y_acceleration & (0b11111111))

        data = [msb_x_accel,
               lsb_x_accel,
               msb_y_accel,
               lsb_y_accel,
               sensors_2.x_gyro,
               sensors_2.y_gyro,
               sensors_2.z_gyro,
               sensors_2.error_code]

    elif (arbitrationID == global_vars.MOTOR_CONTROLLER) or (arbitrationID == global_vars.MOTOR_CONTROLLER_WARN):

        msb_voltage = bytes(motor_controller_data.battery_voltage & (0b11111111 << 8))
        lsb_voltage = bytes(motor_controller_data.battery_voltage& (0b11111111))
        msb_current = bytes(motor_controller_data.battery_current & (0b11111111 << 8))
        lsb_current = bytes(motor_controller_data.battery_current & (0b11111111))
        msb_motor_speed = bytes(motor_controller_data.motor_speed & (0b11111111 << 8))
        lsb_motor_speed = bytes(motor_controller_data.motor_speed & (0b11111111))

        data = [msb_voltage,
                lsb_voltage,
                msb_current,
                lsb_current,
                msb_motor_speed,
                lsb_motor_speed,
                motor_controller_data.motor_controller_temp,
                motor_controller_data.driving_direction
                ]

    else:
        data = [0, 0, 0, 0, 0, 0, 0, 0]

    return data


