from mock_gps import MockGPS

def test_mock_gps_location():
    gps = MockGPS()
    gps.connect()
    location = gps.get_location()
    assert "latitude" in location
    assert "longitude" in location
    assert "timestamp" in location
    gps.disconnect()