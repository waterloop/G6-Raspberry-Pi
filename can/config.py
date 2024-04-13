import time
import can
from ctypes import c_uint8, c_uint16, c_uint32

class BMS_DATA:
    classifer  = "BMS_DATA"
    can_id = 0
    temperature   =   [c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0)] # def these are 8 bits each
    error_code    =    0

class SENSORS_BOARD_DATA:
    classifer = "SENSORS_BOARD_DATA"
    can_id = 0
    temperature = [c_uint16(0), c_uint16(0)]
    imu_data = c_uint16(0)
    pressure_sensor_data = c_uint8(0)
    error_code = c_uint8(0)

class MOTOR_CONTROLLER_DATA:
    classifier = "MOTOR_CONTROLLER_DATA"
    can_id = 0
    battery_voltage = c_uint16(0)
    battery_current = c_uint16(0)
    motor_speed = c_uint16(0)
    motor_controller_temp = c_uint8(0)
    driving_direction = c_uint16(0)
    error_code = c_uint8(0)

class KELLY_DATA_FRAME1:
    driving_direction_kelly = c_uint8(0)
    motor_speed_kelly = c_uint16(0)
    motor_error_code_kelly = c_uint8(0)

class KELLY_DATA_FRAME2:
    battery_voltage_kelly = c_uint16(0)
    battery_current_kelly = c_uint16(0)
    motor_temp_kelly = c_uint16(0)
    motor_controller_temp_kelly = c_uint16(0)

class GLOBAL:
    def __init__(self):
    # GENERAL DEFINES
        MAX_CAN_PAYLOAD_BYTES = 8
        BUFF_SIZE = 32
        WARN_OFFSET = 0xFF

        # MOTOR CONTROLLER
        MOTOR_CONTROLLER_1 = 0x10F8109A
        MOTOR_CONTROLLER_2 = 0x10F8108D
        MOTOR_CONTROLLER = 0xFF
        MOTOR_CONTROLLER_WARN = MOTOR_CONTROLLER - WARN_OFFSET

        # BMS
        BMS_BOARD = 0xFF
        BMS_TEMP = BMS_BOARD
        BMS_BOARD_WARN = BMS_TEMP - WARN_OFFSET

        # SENSORS
        SENSOR_BOARD = 0xFF
        SENSOR_BOARD_WARN = SENSOR_BOARD - WARN_OFFSET

# THIS IS CONFIG.H FOR CROSS REFERENCE

# #pragma once
# #include "can_driver.h"

# // GENERAL DEFINES
# #define MAX_CAN_PAYLOAD_BTYES   8
# #define BUFF_SIZE               32
# #define WARN_OFFSET             0xFF

# // MOTOR CONTROLLER
# #define MOTOR_CONTROLLER_1      0x10F8109A
# #define MOTOR_CONTROLLER_2      0x10F8108D
# #define MOTOR_CONTROLLER        0xFF
# #define MOTOR_CONTROLLER_WARN   MOTOR_CONTROLLER - WARN_OFFSET
# // BMS
# #define BMS_BOARD               0xFF
# #define BMS_BOARD_WARN          BMS_TEMP - WARN_OFFSET
# // SENSORS
# #define SENSOR_BOARD            0xFF
# #define SENSOR_BOARD_WARN       SENSOR_BOARD - WARN_OFFSET

# // BEGIN KELLY DEFS
# // FRAME 1
# const DataSegment DRIVING_DIRECTION_K       = {MOTOR_CONTROLLER_1, 1, 1};
# const DataSegment MOTOR_SPEED_K             = {MOTOR_CONTROLLER_1, 2, 3};
# const DataSegment MOTOR_ERROR_CODE_K        = {MOTOR_CONTROLLER_1, 4, 4}; 
# // FRAME 2
# const DataSegment BATTERY_VOLTAGE_K         = {MOTOR_CONTROLLER_2, 1, 2};
# const DataSegment BATTERY_CURRENT_K         = {MOTOR_CONTROLLER_2, 3, 4};
# const DataSegment MOTOR_TEMP_K              = {MOTOR_CONTROLLER_2, 5, 6};
# const DataSegment MOTOR_CONTROLLER_TEMP_K   = {MOTOR_CONTROLLER_2, 7, 8};
# // END KELLY DEFS

# // BEGIN MOTOR CONTROLLER DEFS
# const DataSegment BATTERY_VOLTAGE           = {MOTOR_CONTROLLER, 1, 2};
# const DataSegment BATTERY_CURRENT           = {MOTOR_CONTROLLER, 3, 4};
# const DataSegment MOTOR_SPEED               = {MOTOR_CONTROLLER, 5, 6};
# const DataSegment MOTOR_CONTROLLER_TEMP     = {MOTOR_CONTROLLER, 7, 7};
# const DataSegment DRIVING_DIRECTION         = {MOTOR_CONTROLLER, 8, 8};
# const DataSegment MOTOR_ERROR_CODE          = {MOTOR_CONTROLLER, 8, 8};
# // END MOTOR CONTROLLER DEFS

# // BEGIN BMS DEFS
# const DataSegment MUX1_TEMP                 = {BMS_BOARD, 1, 1};
# const DataSegment MUX2_TEMP                 = {BMS_BOARD, 2, 2};
# const DataSegment MUX3_TEMP                 = {BMS_BOARD, 3, 3};
# const DataSegment MUX4_TEMP                 = {BMS_BOARD, 4, 4};
# const DataSegment MUX5_TEMP                 = {BMS_BOARD, 5, 5};
# const DataSegment MUX6_TEMP                 = {BMS_BOARD, 6, 6};
# const DataSegment BMS_ERROR_CODE            = {BMS_BOARD, 7, 7};
# // END BMS DEFS

# // BEGIN SENSORS BOARD DEFS
# const DataSegment PRESSURE_SENSOR_DATA      = {SENSOR_BOARD, 1, 1}; 
# const DataSegment IMU_DATA                  = {SENSOR_BOARD, 2, 3};
# const DataSegment LIM_ONE_TEMP              = {SENSOR_BOARD, 4, 5};
# const DataSegment LIM_TWO_TEMP              = {SENSOR_BOARD, 6, 7};
# const DataSegment SENSORS_ERROR_CODE        = {SENSOR_BOARD, 8, 8};
# // END SENSORS BOARD DEFS