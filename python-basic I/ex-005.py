# Write a Python program which accepts the user's first and last name and 
# print them in reverse order with a space between them.

name = input("Input your fullname: ")
name = name.split(" ")

rname = ""

for name in reversed(name):
    rname += name + " "

print(rname)
