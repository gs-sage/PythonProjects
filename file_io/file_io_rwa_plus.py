# notes on how r+, w+ and a+ work

"""r+ opens the file for read and writing. The cursor/pointer is at the beginning of the file.
w+ opens the file for read and write but truncates the file data meaning overwrites the file first.
a+ opens the file for read, write and appends the data to the file."""

f = open("demo2.txt","r+") # the cursor will be at the beginning of the first line and will overwrite starting the first line where the pointer is.
f.write("Hello") # output: Helloile created by python with the write function since it didn't exist before.
print(f.read()) # will print after the point where the cursor currently is.
f.close()

# w+
f = open("demo2.txt","w+")
f.write("This is the w+ function working, It will overwrite what is in the file.")
f.close()

f = open("demo2.txt","r") # we need to read and print the file contents again since write function doesn't return anything besides the word count.
print(f.read()) # prints above line
f.close()

# a+, cursor is at the end of the file
f = open("demo2.txt","a+")
f.write("\nThis will get added to the file")
f.close()

f = open("demo2.txt","r") # we need to read and print the file contents again since write function doesn't return anything besides the word count.
print(f.read()) # prints above line
f.close()