# Write a Python program to print the calendar of a given month and year.

import calendar

theyear = int(input("Input the year, Ex: 2004: "))
themonth = int(input("Input the month, Ex 04: "))

print(calendar.month(theyear, themonth))
