def parse_nmea(sentence):
    if sentence.startswith("$GPGGA"):
        fields = sentence.split(",")
        return {
            "latitude": float(fields[2]) if fields[2] else None,
            "longitude": float(fields[4]) if fields[4] else None,
            "timestamp": fields[1] if fields[1] else None
        }
    return None