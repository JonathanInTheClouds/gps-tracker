import serial
from gps_device import GPSDevice

class SerialGPS(GPSDevice):
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
        print(f"Connected to {self.port} at {self.baudrate} baud")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected")

    def get_location(self):
        if not self.connection:
            raise ValueError("Device is not connected")
        
        raw_data = self.connection.readline().decode('utf-8').strip()
        return 
    
    def _parse_nmea(self, sentence):
        return {"latitute": 0.0, "longitude": 0.0, "timestamp": "00:00:00"}