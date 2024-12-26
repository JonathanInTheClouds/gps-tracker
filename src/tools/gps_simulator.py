import time
import random

def simulate_gps():
    while True:
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        print(f"{{'latitude': {latitude}, 'longitude': {longitude}, 'timestamp': '{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}'}}")
        time.sleep(1)

if __name__ == "__main__":
    simulate_gps()