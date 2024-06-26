import can
import time
bus = can.interface.Bus(channel="can0", bustype="socketcan", receive_own_messages=True)
msg = can.Message(arbitration_id=0x7de, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False)

try:
    while True:
        time.sleep(1)
        bus.send(msg)
        print("Message sent")
except can.CanError as e:
    print("Message failed to send", e)

bus.shutdown()
