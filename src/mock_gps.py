from gps_device import GPSDevice
import time
import random

class MockGPS(GPSDevice):
    def connect(self):
        print("Connected to Mock GPS.")

    def disconnect(self):
        print("Disconnected from Mock GPS.")

    def get_location(self):
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        return {
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
