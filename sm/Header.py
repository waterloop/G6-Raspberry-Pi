# # STATES (MAY REFACTOR TO A DICT)
# CURRENT_STATE = 0
# BOOT = 0
# LV_CHECK = 1
# LV_READY = 2
# HV_CHECK = 3
# HV_READY = 4
# AUTOPILOT = 5
# BRAKE = 6]


# RECIEVE_CAN = 7

# MANUAL_CONTROL = 10
# PENDING_COMMAND = 11
# VALIDATE_COMMAND = 12

# MANUAL_CONTROLS_AUTOPILOT = 20
# MANUAL_CONTROLS_ACCELERATE = 21
# MANUAL_CONTROLS_DECELERATE = 22
# MANUAL_CONTROLS_BRAKE = 23


# IMPORTS

import time


class State:
    current_state = 0
    def select(self):
        if self.current_state == 0:
            return self.BOOT()
        elif self.current_state == 1:
            return self.LV_CHECK()
        elif self.current_state == 2:
            return self.LV_READY()
        elif self.current_state == 3:
            return self.HV_CHECK()
        elif self.current_state == 4:
            return self.HV_READY()
        
    def BOOT(self):
        time.sleep(10)
        self.current_state = 1
        return "this is boot"

    def LV_CHECK(self): # LV_CHECK function
        time.sleep(5)
        self.current_state = 2
        return "This is LV CHECK"

    def LV_READY(self):
        time.sleep(5)
        self.current_state = 3
        return "This is LV_READY"

    def HV_CHECK(self):
        time.sleep(5)
        self.current_state = 4
        return "This is HV_CHECK"
    
    def HV_READY(self):
        time.sleep(5)
        self.current_state = 5
        return "This is HV_READY"
    
    def AUTOPILOT(self):
        time.sleep(10)
        self.current_state = 6
        return "This is autopilot"