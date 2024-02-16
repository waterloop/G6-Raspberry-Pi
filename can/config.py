import time
import can

BMS_ARBITRATION_ID = 100

class BMS_DATA:
    classifer  = "BMS_DATA"
    arbitration_id = BMS_ARBITRATION_ID
    temperature =   [0,0,0,0,0,0]
    error       =    0


