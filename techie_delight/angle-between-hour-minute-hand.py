#!/usr/bin/python

import sys

def calc_angle(time):
    hour, minute = time.split(":")
    hour_angle = (int(hour) * 30) + ((int(minute) * 360) / (12*60))
    minute_angle = int(minute) * 6
    diff = 0
    if hour_angle > 180:
        diff = abs(360 - hour_angle - minute_angle)
    else:
        diff = abs(hour_angle - minute_angle)
    print diff

def main():
    calc_angle("5:30")
    calc_angle("9:00")
    calc_angle("12:00")
    
if __name__ == "__main__":
    main()
    
    