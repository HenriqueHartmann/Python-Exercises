# Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi

r = float(input("Input the radius value: "))
a = pi * pow(r, 2)
print("Area = {}".format(a))
