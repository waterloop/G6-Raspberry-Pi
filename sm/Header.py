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
        if self.current_case == 0:
            return self.default_case()
        elif self.current_case == 1:
            return self.LV_CHECK()
        elif self.current_case == 2:
            return self.case2()
        elif self.current_case == 3:
            return self.case3()
    def LV_CHECK(self): # LV_CHECK function
        time.sleep(5000)
        self.current_state = 1
        return 0
        

        return "This is case 1"

    def case2(self):
        return "This is case 2"

    def case3(self):
        return "This is case 3"
    
    def default_case(self):
        return "This is the default case"