import time
import can
from ctypes import c_uint8, c_uint16

class BMS_DATA:
    can_id = 0
    temperature   =   [c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0)]
    error_code    =    c_uint8(0)

class SENSORS_1: #CONSISTS OF PRESSURE, LIM1, AND LIM2
    can_id = 0
    pressure_sensor_data = c_uint16(0)
    lim_temperature = [c_uint16(0), c_uint16(0)]
    error_code = c_uint8(0)

class SENSORS_2: #CONSISTS OF IMU
    can_id = 0
    x_acceleration = c_uint16(0)
    y_acceleration = c_uint16(0)
    x_gyro = c_uint8(0)
    y_gyro = c_uint8(0)
    z_gyro = c_uint8(0)
    error_code = c_uint8(0)

class MOTOR_CONTROLLER_DATA:
    can_id = 0
    battery_voltage = c_uint16(0)
    battery_current = c_uint16(0)
    motor_speed = c_uint16(0)
    motor_controller_temp = c_uint8(0)
    driving_direction = c_uint8(0)
    error_code = c_uint8(0) #Note: the error code and driving direction are obtained from the same byte in the config.h datasegment.

class GLOBAL:
    def __init__(self):
    # GENERAL DEFINES
        self.MAX_CAN_PAYLOAD_BYTES = 8
        self.BUFF_SIZE = 32
        self.WARN_OFFSET = 0xFF

    #CAN ID DEFINES

        # MOTOR CONTROLLER
        self.MOTOR_CONTROLLER = 0xFF
        self.MOTOR_CONTROLLER_WARN = self.MOTOR_CONTROLLER - self.WARN_OFFSET

        # BMS
        self.BMS_BOARD = 0
        self.BMS_BOARD_WARN = self.BMS_BOARD - self.WARN_OFFSET

        # SENSOR BOARD 1
        self.SENSOR_BOARD_1 = 0
        self.SENSOR_BOARD_1_WARN = self.SENSOR_BOARD_1 - self.WARN_OFFSET

        # SENSOR BOARD 2
        self.SENSOR_BOARD_2 = 0
        self.SENSOR_BOARD_2_WARN = self.SENSOR_BOARD_2 - self.WARN_OFFSET


# THIS IS CONFIG.H FOR CROSS REFERENCE

# #pragma once
# #include "can_driver.h"

# // GENERAL DEFINES
# #define MAX_CAN_PAYLOAD_BTYES   8
# #define BUFF_SIZE               32
# #define WARN_OFFSET             0xFF

# // MOTOR CONTROLLER
# #define MOTOR_CONTROLLER_K1     0x10F8109A
# #define MOTOR_CONTROLLER_K2     0x10F8108D
# #define MOTOR_CONTROLLER        0xFF
# #define MOTOR_CONTROLLER_WARN   MOTOR_CONTROLLER - WARN_OFFSET
# // BMS
# #define BMS_BOARD               0xFF
# #define BMS_BOARD_WARN          BMS_TEMP - WARN_OFFSET
# // SENSORS
# #define SENSOR_BOARD_1          0xFF
# #define SENSOR_BOARD_1_WARN     SENSOR_BOARD_1 - WARN_OFFSET
# #define SENSOR_BOARD_2          0xFF
# #define SENSOR_BOARD_2_WARN     SENSOR_BOARD_2 - WARN_OFFSET

# // BEGIN KELLY DEFS
# // FRAME 1
# const Data_Segment_t DRIVING_DIRECTION_K       = {MOTOR_CONTROLLER_K1, 1, 1};
# const Data_Segment_t MOTOR_SPEED_K             = {MOTOR_CONTROLLER_K1, 2, 3};
# const Data_Segment_t MOTOR_ERROR_CODE_K        = {MOTOR_CONTROLLER_K1, 4, 4}; 
# // FRAME 2
# const Data_Segment_t BATTERY_VOLTAGE_K         = {MOTOR_CONTROLLER_K2, 1, 2};
# const Data_Segment_t BATTERY_CURRENT_K         = {MOTOR_CONTROLLER_K2, 3, 4};
# const Data_Segment_t MOTOR_TEMP_K              = {MOTOR_CONTROLLER_K2, 5, 6};
# const Data_Segment_t MOTOR_CONTROLLER_TEMP_K   = {MOTOR_CONTROLLER_K2, 7, 8};
# // END KELLY DEFS

# // BEGIN MOTOR CONTROLLER DEFS
# const Data_Segment_t BATTERY_VOLTAGE           = {MOTOR_CONTROLLER, 1, 2};
# const Data_Segment_t BATTERY_CURRENT           = {MOTOR_CONTROLLER, 3, 4};
# const Data_Segment_t MOTOR_SPEED               = {MOTOR_CONTROLLER, 5, 6};
# const Data_Segment_t MOTOR_CONTROLLER_TEMP     = {MOTOR_CONTROLLER, 7, 7};
# const Data_Segment_t DRIVING_DIRECTION         = {MOTOR_CONTROLLER, 8, 8};
# const Data_Segment_t MOTOR_ERROR_CODE          = {MOTOR_CONTROLLER, 8, 8};
# // END MOTOR CONTROLLER DEFS

# // BEGIN BMS DEFS
# const Data_Segment_t MUX1_TEMP                 = {BMS_BOARD, 1, 1};
# const Data_Segment_t MUX2_TEMP                 = {BMS_BOARD, 2, 2};
# const Data_Segment_t MUX3_TEMP                 = {BMS_BOARD, 3, 3};
# const Data_Segment_t MUX4_TEMP                 = {BMS_BOARD, 4, 4};
# const Data_Segment_t MUX5_TEMP                 = {BMS_BOARD, 5, 5};
# const Data_Segment_t MUX6_TEMP                 = {BMS_BOARD, 6, 6};
# const Data_Segment_t BMS_ERROR_CODE            = {BMS_BOARD, 8, 8};
# // END BMS DEFS

# // BEGIN SENSORS BOARD DEFS
# //FIRST FRAME
# const Data_Segment_t PRESSURE_SENSOR_DATA      = {SENSOR_BOARD_1, 1, 2}; 
# const Data_Segment_t LIM_ONE_TEMP              = {SENSOR_BOARD_1, 3, 4};
# const Data_Segment_t LIM_TWO_TEMP              = {SENSOR_BOARD_1, 5, 6};
# const Data_Segment_t SENSORS_ERROR_CODE_1      = {SENSOR_BOARD_1, 8, 8};
# //SECOND (IMU) FRAME
# const Data_Segment_t X_ACCEL                   = {SENSOR_BOARD_2, 1, 2}; 
# const Data_Segment_t Y_ACCEL                   = {SENSOR_BOARD_2, 3, 4};
# const Data_Segment_t X_GYRO                    = {SENSOR_BOARD_2, 5, 5};
# const Data_Segment_t Y_GYRO                    = {SENSOR_BOARD_2, 6, 6};
# const Data_Segment_t Z_GYRO                    = {SENSOR_BOARD_2, 7, 7};
# const Data_Segment_t SENSORS_ERROR_CODE_2      = {SENSOR_BOARD_2, 8, 8};
# // END SENSORS BOARD DEFS