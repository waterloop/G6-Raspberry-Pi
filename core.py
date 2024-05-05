import can
import time

def main():
    time.sleep(5)
    bus = can.interface.Bus(channel="can0", bustype="socketcan", loopback=True)
    notifier = can.Notifier(bus, [can.Printer()])
    
    try:
        # Simulate doing some work
        time.sleep(10)
    finally:
        # Ensure the notifier is stopped first
        notifier.stop()
        # Then shut down the bus
        bus.shutdown()

if __name__ == "__main__":
    main()
