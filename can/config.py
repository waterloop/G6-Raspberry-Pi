import time
import can
import ctypes

class BMS_DATA:
    classifer  = "BMS_DATA"
    can_id = 0
    temperature =   [c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0), c_uint8(0)] # def these are 8 bits each
    error       =    0


class SENSORS_BOARD_DATA:
    classifer = "SENSORS_BOARD_DATA"
    can_id = 0
    temperature = [c_uint16(0), c_uint16(0)]
    imu_data = c_uint16(0)
    pressure_sensor_data = c_uint8(0)
    error_code = c_uint8(0)



class GLOBAL:
    def GLOBAL(self):
        self.BMS_CAN_ID=100
        self.SENSORS_BOARD_CAN_ID=50