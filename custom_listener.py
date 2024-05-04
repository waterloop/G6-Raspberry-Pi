import can
import time

# Define a listener class that can handle messages
class SomeListener(can.Listener):
    def on_message_received(self, msg):
        print(msg)

# Setup the CAN bus
my_bus = can.Bus(channel='can0', bustype='socketcan', receive_own_messages=True)

# Instantiate the listener object
listener = SomeListener()

# Use a Notifier to handle messages asynchronously
notifier = can.Notifier(my_bus, [listener])

try:
    # The script now runs and listens for messages indefinitely
    while True:
        time.sleep(1)  # Pause the loop to prevent it from running too fast
except KeyboardInterrupt:
    # Stop the notifier to clean up resources when you stop the script manually
    notifier.stop()
    print("Stopped listening on CAN bus.")
