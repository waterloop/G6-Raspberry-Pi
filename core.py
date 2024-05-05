import can

bus = can.interface.Bus(channel="can0", bustype="socketcan_native")
notifier = can.Notifier(bus, [can.Printer()])