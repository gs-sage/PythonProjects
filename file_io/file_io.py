"""File I/O (input-ouput)
Python can be used to perform operations on a file.

Types of files:
1. Text files: .txt, .docx, .log etc --> data are stored in characters 
2. Binary files: .mp4, .mov, .png, .jpeg etc --> data are not stored in characters but are stored in other formats 

Actions that we can do on a file: open, read, write, close

Syntax to do actions to a file;
f = open("file name", "mode/action")
so to do actions on a file we need to provide the full name of the file and the mode/action we want.
If we don't provide any action to python, it assumes we just want to do the read action on the file.""" 

f = open("demo.txt", "r") # opening the file in read mode
data = f.read() # reading the file
print(data) # printing the contents of the file
print(type(data)) # printing the type of the file
f.close() # closing the file.

"""Character and Meanings:
r : open for reading(default)
w : open for writing, truncating the file first
x : create a new file and open it for writing
a : open for writing, appending to the end of the file if it exists
b : binary mode
t : text mode (default mode for files)
+ : open a disk file for updating(reading and writing)"""