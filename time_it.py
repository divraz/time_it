import math
from decimal import Decimal
from datetime import datetime

def squared_power_list (num, start = 0, end = 0):
    s_list = []
    for i in range (start, end + 1):
        s_list.append (pow (num, i))
    return s_list

def polygon_area (s_len, sides = 3):
    if s_len <= 0 or sides < 3:
        raise ValueError ('len > 0 and sides >= 3')
    apothem = s_len / (2 * math.tan (math.pi / sides))
    area = sides * s_len * apothem / 2
    return area

def temp_converter (temp, temp_given_in = 'f'):
    if temp_given_in == 'f':
        temp = (temp - 32) * 5 / 9
    elif temp_given_in == 'c':
        temp = temp * 9 / 5 + 32
    return temp

def speed_converter (speed : 'kmph', dist = 'km', time = 'hr'):
    if speed < 0:
        raise ValueError ('speed cannot be negative')
    if dist == 'km':
        speed *= 1
    elif dist == 'm':
        speed *= 1000
    elif dist == 'ft':
        speed *= 3280.84
    elif dist == 'yrd':
        speed *= 1093.61

    if time == 'hr':
        speed /= 1
    elif time == 'm':
        speed /= 60
    elif time == 's':
        speed /= 3600
    elif time == 'ms':
        speed /= 3600000
    elif time == 'day':
        speed *= 24

    return (speed)

def time_it (fn, *args, repetitions = 1, **kwargs):
    start = datetime.now ()
    for i in range (repetitions):
        fn (*args, **kwargs)
    end = datetime.now ()
    return Decimal (str (end - start).split (':')[-1]) / repetitions
