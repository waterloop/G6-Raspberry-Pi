# IMPORTS
# import RPi.GPIO as GPIO
import time
import threading
# from Header import State 

def f1():
    while True:
        print("t1")
        time.sleep(1)
def f2():
    while True:
        print("t2")
        time.sleep(2)
def f3():
    while True:
        print("t3")
        time.sleep(3)
def f4():
    while True:
        print("t4")
        time.sleep(4)
def f5():
    while True:
        print("t5")
        time.sleep(5)
def f6():
    while True:
        print("t6")
        time.sleep(6)
t1 = threading.Thread(target=f1)
t1.start()
t2 = threading.Thread(target=f2)
t2.start()
t3 = threading.Thread(target=f3)
t3.start()
t4 = threading.Thread(target=f4)
t4.start()
t5 = threading.Thread(target=f5)
t5.start()
t6 = threading.Thread(target=f6)
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()