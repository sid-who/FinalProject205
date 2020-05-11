#
# Code by Gurpreet Sidhu, Jose Perez, Cesar Borrego, and Justin Thon
# File name: project_main.py
# Date Created: 5/9/20
# Python version 3.7
# CST 205 - Multimedia Design & Programming
# Purpose: Test function for calculating the linear gradient, source below.
#

#https://bsou.io/posts/color-gradients-with-python
import matplotlib.pyplot as plt

def linear_gradient(start_tuple, end_tuple, n):
	RGB_List = [start_tuple]

	hex_list = []

	for t in range(1, n):
		curr_vector = [
			int(start_tuple[j] + (float(t)/(n-1))*(end_tuple[j] - start_tuple[j]))
			for j in range(3)
		]
		RGB_List.append(curr_vector)
	print(RGB_List)
	for i in range(len(RGB_List)):
		red = RGB_List[i][0]
		green = RGB_List[i][1]
		blue = RGB_List[i][2]
		color = (red, green, blue)
		converted_color = '#%02x%02x%02x' % color
		hex_list.append(converted_color)
	print(hex_list)


linear_gradient((207,245,199), (22,89,9), 10)