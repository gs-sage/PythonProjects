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

"""We can also take how many characters from a file."""
f = open("demo.txt","r") # need to open the file again since we closed it above
data = f.read(5) # takes the first 5 characters in the file
print(data)
f.close() # closing the file

"""We can also read lines as we need with the readline() function"""
f = open("demo.txt","r")
line1 = f.readline() # this will print the first line and the space after it cause each line has a \n at the end when it goes to the next line
print(line1)
line2 = f.readline() # this prints the second line cause from research I found, readline() prints from the last place where the cursor was and moves forward.  
# In this case the cursor was at line 1 and it already printed and so it moved forward and went to next line so it printed line 2. 
print(line2) # so it printed line 2 from the file here
f.close()

"""IMPORTANT
If we read a file, print it and then use the readline() function, we will get
empty lines cause, when you read a file, the cursor/pointer has already read the file to the 
end of the file and the only thing at the end of the file is the newline character(\n), so the
readline() function now reads the next line characters and just prints empty lines.

Visually they would be somethine like if a file had 3 lines with either sentences or characters:
|   abc     | # so when we use f.read() the whole file is read, that is
|   def     | # abc\ndef\nghi\n <-- and the cursor is at the end
|___ghi_____| # and when readline() comes and reads it now it just reads the newline character
"""

