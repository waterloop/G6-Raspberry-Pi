import time
import can
import ctypes

BMS_CAN_ID = 100
SENSORS_BOARD_CAN_ID
class BMS_DATA:
    classifer  = "BMS_DATA"
    can_id = BMS_CAN_ID
    temperature =   [c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0)] # def these are 8 bits each
    error       =    0


# Define BMS instances 
bms_data = BMS_DATA()
bms_data_warn = BMS_DATA()

# Assign temp values for each instance
bms_data.temperature = [MUX1_TEMP, MUX2_TEMP, MUX3_TEMP, MUX4_TEMP, MUX5_TEMP, MUX6_TEMP]
bms_data_warn.temperature = [MUX1_TEMP_WARN, MUX2_TEMP_WARN, MUX3_TEMP_WARN, MUX4_TEMP_WARN, MUX5_TEMP_WARN, MUX6_TEMP_WARN]


class SENSORS_BOARD_DATA:
    classifer = "SENSORS_BOARD_DATA"
    can_id = SENSORS_BOARD_CAN_ID
    temperature = [c_uint16(0), c_uint16(0)]
    imu_data = c_uint16(0)
    pressure_sensor_data = c_uint8(0)
    error_code = c_uint8(0)