import yaml
from gps_factory import get_gps_device

def main():
    # Load configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Get the appropriate GPS device
    gps_device = get_gps_device(config)

    try:
        # Connect and get location
        gps_device.connect()
        location = gps_device.get_location()
        print(f"Current Location: {location}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        gps_device.disconnect()

if __name__ == "__main__":
    main()