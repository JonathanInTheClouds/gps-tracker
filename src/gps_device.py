from abc import ABC, abstractmethod

class GPSDevice(ABC):
    @abstractmethod
    def connect(self):
        """Establish a connection to the GPS device"""
        pass

    @abstractmethod
    def disconnect(self):
        """Terminate connection to the GPS device"""
        pass

    @abstractmethod
    def get_location(self):
        """Return the current location of the GPS device"""
        pass