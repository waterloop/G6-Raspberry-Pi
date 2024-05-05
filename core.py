import can

bus = can.interface.Bus(channel="can0", bustype="socketcan")
notifier = can.Notifier(bus, [can.Printer()])