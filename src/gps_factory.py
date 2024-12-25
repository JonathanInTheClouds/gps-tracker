from serial_gps import SerialGPS
from built_in_gps import BuiltInGPS

def get_gps_device(config):
    device_type = config.get("device_type", "usb_serial")
    if device_type == "usb_serial":
        return SerialGPS(port=config.get("port", "/dev/ttyUSB0"))
    elif device_type == "built_in":
        return BuiltInGPS()
    else:
        raise ValueError(f"Unsupported device type: {device_type}")