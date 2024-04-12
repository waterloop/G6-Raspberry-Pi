# here we go
# beta authored by Alexander (Xander) Hayhoe

# start date: April 10th, 2024 😈😈😈

# IMPORTS
# import RPi.GPIO as GPIO
import time
from threading import Thread
from Header import State 

# GLOBALS


# STATES (MAY REFACTOR TO A DICT)
CURRENT_STATE = 0
BOOT = 0
LV_CHECK = 1
LV_READY = 2
HV_CHECK = 3
HV_READY = 4
AUTOPILOT = 5
BRAKE = 6

RECIEVE_CAN = 7

MANUAL_CONTROL = 10
PENDING_COMMAND = 11
VALIDATE_COMMAND = 12

MANUAL_CONTROLS_AUTOPILOT = 20
MANUAL_CONTROLS_ACCELERATE = 21
MANUAL_CONTROLS_DECELERATE = 22
MANUAL_CONTROLS_BRAKE = 23

# BETA PIN DEFINITIONS

LV_CHECK_PIN = 4
LV_READY_PIN = 5
HV_CHECK_PIN = 6
HV_READY_PIN = 7
AUTOPILOT_PIN = 10


def send_can():
    # simulate sending a message


    return 0

def LV_CHECK(): # LV_CHECK function
    time.sleep(5000)
    CURRENT_STATE = 1
    return 0

def LV_CHECK_RUNNER(): # LED that indicates that LV_CHECK is running
    GPIO.output(LV_CHECK_PIN, GPIO.HIGH) 
    time.sleep(300)
    GPIO.output(LV_CHECK_PIN, GPIO.LOW)  
    time.sleep(300)

def main():
    assert CURRENT_STATE == 0, "STATE MUST START AT 0"
    state = State()
    print(state.case1())





if __name__ == "__main__":
    main()