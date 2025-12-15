# Writing to a file
# this function in file i/o overwrites the file

"""It works the same way as read. 
We first need to open the file, and the write to it."""

f = open("demo.txt","w")
data = f.write("This is a line written with the write feature in file i/o in python.") # this will only write to the file and returns the character count
# print(data) # will return character count, uncomment to see
f.close()

"""IMPORTANT
write() function is python doesn't return the string, we wrote, it returns the count of the
characters. To have the data printed from file we wrote to, we close the current open write function
and open the file in read mode and print it."""

f = open("demo.txt","r")
data = f.read()
print(data)
f.close()

"""If the file doesn't exist and we use write to do functions, python will create the file"""
# this will create demo2.txt since it currently doesn't exist.
f = open("demo2.txt","w")
f.write("New file created by python with the write function since it didn't exist before.")
f.close()
