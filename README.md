## Functions
- time_it
	- a function which gives out average run time per call
	- time_it (fn, *args, repetitions = 1, **kwargs)
- speed_converter
	- convert a speed given in km/hr to km/m/ft/yrd per ms/s/m/hr/day
	- speed_converter (speed : 'kmph', dist = 'km', time = 'hr')
- temp_converter
	- convert temperature from celsius to fahrenheit and wise versa
	- temp_converter (temp, temp_given_in = 'f')
- polygon_area
	- find area of a regular polygon
	- polygon_area (s_len, sides = 3)
- squared_power_list
	- generate list of numbers squared
	- squared_power_list (num, start = 0, end = 0)

## Test Functions
- print
	- test_time_it_print
		- average time for 100 iterations = average time for 1000 iterations

- squared_power_list
	- test_base_squared_power_list
		- function with no argument should throw TypeError
	- test_base_time_it_squared_power_list
		- function with no argument in time_it should throw TypeError
	- test_1_squared_power_list
		- function with only one positional argument should give a list = [1]
	- test_time_squared_power
		- average time for 100 iterations = average time for 1000 iterations

- polygon_area
	- test_base_polygon_area
		- function with no argument should throw TypeError
	- test_base_time_it_polygon_area
		- function with no argument in time_it should throw TypeError
	- test_1_polygon_area
		- area of triangle
	- test_2_polygon_area
		- area of square
	- test_3_polygon_area
		- area of pentagon
	- test_4_polygon_area
		- area of hexagon
	- test_5_polygon_area
		- area with negative value of side should give ValueError
	- test_time_polygon_area
		- average time for 100 iterations = average time for 1000 iterations

- temp_converter
	- test_base_temp_converter
		- function with no argument should throw TypeError
	- test_temp_converter_f
		- convert a temprature from fahrenheit to celsius and wise versa
	- test_time_temp_converter
		- average time for 100 iterations = average time for 1000 iterations

- speed_converter
	- test_base_speed_converter
		- function with no argument should throw TypeError
	- test_negative_speed_converter
		- function with negative speed should throw ValueError
	- test_1_speed_converter
		- conversion from km/hr to foot/sec
