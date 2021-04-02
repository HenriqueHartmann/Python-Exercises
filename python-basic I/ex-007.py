# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

filename = input("Input the name of the file with extension: ")
extension = filename.split(".", 1)
print(extension[1])
