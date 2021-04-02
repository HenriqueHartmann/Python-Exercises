# Write a Python program which accepts a sequence of comma-separated numbers from user and
# generate a list and a tuple with those numbers.

dsample = input("Input a group of number separated by coma: ")
dlist = dsample.split(",")
dtuple = tuple(dlist)

print(dsample)
print(dlist)
print(dtuple)
