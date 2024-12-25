import subprocess
import json
from gps_device import GPSDevice

class BuiltInGPS(GPSDevice):
    def __init__(self):
        self.process = None

    def connect(self):
        try:
            self.process = subprocess.Popen(['gpspipe', '-w'], stdout=subprocess.PIPE, text=True)
            print("Connected to built-in GPS.")
        except FileNotFoundError:
            raise ConnectionError("GPSD is not installed or running.")  

    def disconnect(self):
        if self.process:
            self.process.terminate()
            print("Disconnected from built-in GPS.")

    def get_location(self):
        if not self.process:
            raise ConnectionError("Built-in GPS is not connected.")

        for line in self.process.stdout:
            try:
                data = json.loads(line.strip())
                if 'lat' in data and 'lon' in data:
                    return {
                        "latitude": data['lat'],
                        "longitude": data['lon'],
                        "timestamp": data['time']
                    }
            except json.JSONDecodeError:
                continue
        raise RuntimeError("Failed to retrieve location from built-in GPS.")
