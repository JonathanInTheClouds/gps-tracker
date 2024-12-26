from nmea_parser import parse_nmea

def test_parse_nmea():
    sentence = "$GPGGA,123456.78,0123.4567,N,12345.6789,W,1,08,0.9,545.4,M,46.9,M,,*47"
    data = parse_nmea(sentence)
    assert data["latitude"] == 123.4567
    assert data["longitude"] == 12345.6789
    assert data["timestamp"] == "123456.78"