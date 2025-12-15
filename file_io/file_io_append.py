# append function in file i/o

"""Adds data to the end of the file"""

f = open("demo.txt","a")
f.write("Adding this new line. This will be in the same line without a space at the beginning of this line since we don't have the \\n character") # using escape character for \n otherwise it would send the next part to new line
f.write("\nThis will be in a new line since we have the newline character in the front. Or we can keept it at the end.\n")
f.write("And the next lines comes to the new next line.")
f.close()

"""IMPORTANT
append function also can create files if they don't exist."""