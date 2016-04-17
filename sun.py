#!/usr/bin/env python
from sunrise import sun
from datetime import datetime

def is_in_daylight(time=datetime.now().time(), lat=51.5074, lng=0.1278):
    s = sun(lat=lat, long=lng)
    return time > s.sunrise() and time < s.sunset()

if __name__ == "__main__":
    print is_in_daylight()
