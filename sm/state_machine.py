# here we go
# beta authored by Alexander (Xander) Hayhoe

# start date: April 10th, 2024 😈😈😈

# IMPORTS
import RPi.GPIO as GPIO
import time
import threading
from Header import State, change_state_runner

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

def import_func_from_can_listener_for_duty_cycle():
    while True:
        print("CAN LISTENER")
        time.sleep(10)
    return -2
def import_func_from_bt_listener_for_duty_cycle():
    while True:
        print("BT LISTENER")
        time.sleep(10)
    return -3
def heartbeat_BT_conn():
    while True:
        print("BT Heartbeat")
        time.sleep(10)
    return -4


def send_can():
    # simulate sending a message


    return 0


def STARTUP_CHECK_RUNNER(stop_event, PIN): # LED that indicates that LV_CHECK is running. This is what the State machine runs while another thread runs LV check processes
    while not stop_event.is_set():
        GPIO.output(PIN, GPIO.HIGH) 
        time.sleep(0.3)
        GPIO.output(PIN, GPIO.LOW)  
        time.sleep(0.3)
    GPIO.cleanup()
def THREAD_RUNNER(target_function, func_args, state):
    stop_event = threading.Event()

    t1 = threading.Thread(target=target_function, args=(stop_event, func_args))
    t2 = threading.Thread(target=change_state_runner, args=state)
    t1.start()
    t2.start()
    t2.join() # t2 finishes
    stop_event.set() # set event to end
    
    t1.join() # wait for t1 to finish

    return state

def main():
    state = State()
    assert state.current_state == 0, "STATE MUST START AT 0"

    # begin startup sequence for pod. We shall define two thread in this case. 
    # one thread will be responsible for running the state command. the other thread will run until the state command finishes. we will invoke the 
    # {STATE}_RUNNER function to accomplish this
    state = state.select() # run boot, single threaded

    state = THREAD_RUNNER(STARTUP_CHECK_RUNNER, LV_CHECK_PIN, state=state) # state 1 -> 2

    state = THREAD_RUNNER(STARTUP_CHECK_RUNNER, LV_READY_PIN, state=state) # state 2 -> 3

    state = THREAD_RUNNER(STARTUP_CHECK_RUNNER, HV_CHECK_PIN, state=state) # state 3 -> 4

    state = THREAD_RUNNER(STARTUP_CHECK_RUNNER, HV_READY_PIN, state=state) # state 4 -> 5

    # time to transition into autopilot

    state = THREAD_RUNNER(STARTUP_CHECK_RUNNER, AUTOPILOT_PIN, state=state) # autpilot is now active. startup is complete

    # now, we enter a predefined duty loop. 
    # now, we need to invoke the processes responsible for the CAN and Bluetooth listener.
    CAN_listener_process = threading.Thread(target=import_func_from_can_listener_for_duty_cycle, args="args")
    BT_listener_process = threading.Thread(target=import_func_from_bt_listener_for_duty_cycle, args="args") 
    HB_listener_process = threading.Thread(target=heartbeat_BT_conn, args="args")
    while(True):
        print("aAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        time.sleep(1)
        # duty cycle




    # t1 = threading.Thread(target=STARTUP_CHECK_RUNNER, args=(stop_event, LV_CHECK_PIN)) 
    # t2 = threading.Thread(target=state.select)
    # t1.start()
    # t2.start()

    # t2.join() # t2 finishes
    # stop_event.set() # set event to end
    
    # t1.join() # wait for t1 to finish

     




if __name__ == "__main__":
    main()