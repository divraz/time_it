import subprocess
import sys
import pytest
import Qualean
from time_it import *
from decimal import Decimal
import time
import os.path
import re
import inspect 
import random
random.seed(10)
import math
from datetime import datetime

README_CONTENT_CHECK_FOR = [
'squared_power_list',
'polygon_area',
'temp_converter',
'speed_converter',
'time_it'
]

def test_time_it_print ():
    t1 = int (time_it (print, 1, 2, 3, sep = '-', end = '***\n', repetitions=100) * 100000)
    t2 = int (time_it (print, 1, 2, 3, sep = '-', end = '***\n', repetitions=1000) * 100000)
    assert t1 == t2 or t1 == t2 - 1 or t1 == t2 + 1, (t1, t1, "print time_it nor working properly")

def test_base_squared_power_list ():
    with pytest.raises(TypeError) as e_info:
        x = squared_power_list ()

def test_base_time_it_squared_power_list ():
    with pytest.raises(TypeError) as e_info:
        x = time_it (squared_power_list, repetitions = 1)

def test_1_squared_power_list ():
    x = squared_power_list (2)
    assert len (x) == 1 and x[0] == 1, "lenght of list should be 1 by default"

def test_time_squared_power ():
    t1 = int (time_it (squared_power_list, 2, start = 0, end = 5, repetitions = 100) * 100000)
    t2 = int (time_it (squared_power_list, 2, start = 0, end = 5, repetitions = 1000) * 100000)
    assert t1 == t2 or t1 == t2 - 1 or t1 == t2 + 1, (t1, t1, "squared_power time_it nor working properly")

def test_base_polygon_area ():
    with pytest.raises(TypeError) as e_info:
        x = polygon_area ()

def test_base_time_it_polygon_area ():
    with pytest.raises(TypeError) as e_info:
        x = time_it (polygon_area)

def test_1_polygon_area ():
    x = polygon_area (10)
    assert round (x, 1) == 43.3, (x, "Area of triangle is wrong")

def test_2_polygon_area ():
    x = polygon_area (10, sides = 4)
    assert round (x, 1) == 100, (x, "Area of square is wrong")

def test_3_polygon_area ():
    x = polygon_area (10, sides = 5)
    assert round (x, 1) == 172, (x, "Area of pentagon is wrong")

def test_4_polygon_area ():
    x = polygon_area (10, sides = 6)
    assert round (x, 1) == 259.8, (x, "Area of hexagon is wrong")

def test_5_polygon_area ():
    with pytest.raises(ValueError) as e_info:
        x = polygon_area (1, -2)

def test_time_polygon_area ():
    t1 = int (time_it (polygon_area, 10, sides = 6, repetitions = 100) * 100000)
    t2 = int (time_it (polygon_area, 10, sides = 6, repetitions = 1000) * 100000)
    assert t1 == t2 or t1 == t2 - 1 or t1 == t2 + 1, (t1, t1, "polygon_area time_it nor working properly")

def test_base_temp_converter ():
    with pytest.raises(TypeError) as e_info:
        x = temp_converter ()

def test_temp_converter_f ():
    x = temp_converter (32, 'f')
    x = temp_converter (x, 'c')
    assert x == 32, "temp_converter not working properly"

def test_time_temp_converter ():
    t1 = int (time_it (temp_converter, 100, temp_given_in = 'f', repetitions = 100) * 100000)
    t2 = int (time_it (temp_converter, 100, temp_given_in = 'f', repetitions = 1000) * 100000)
    assert t1 == t2 or t1 == t2 - 1 or t1 == t2 + 1, (t1, t1, "polygon_area time_it nor working properly")

def test_base_speed_converter ():
    with pytest.raises(TypeError) as e_info:
        x = speed_converter ()

def test_negative_speed_converter ():
    with pytest.raises(ValueError) as e_info:
        x = speed_converter (-1)

def test_1_speed_converter ():
    x = speed_converter (100, dist = 'ft', time = 's')
    assert int (x) == 91, "speed converter not working properly"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 10, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print (c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 3

def test_fourspace():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Qualean)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Qualean, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

if __name__ ==  '__main__':
    test_clear_memory()
