# creating a program that creates a file and writes to it

# Practice 1: Create a file and write some data to it.
# creating the file and opening in write mode to add data
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")

with open("practice.txt","r") as f: # opening the file in read mode to read contents of the file
    data = f.read()
    print(data)

# Practice 2: Open the same file you created and edit the word Java to python
# opening the file in r+ for read and write as I need to read the data and then edit it
# the replace function in this case needs to be in the variable right after f.read()
with open("practice.txt","r+") as f:    
    data = f.read().replace("Java","Python")
    print(data)

"""IMPORTANT: In the above number 2, we just replaced the values but didn't write it to the file.
If we want to write it to the file, we would have done something like:

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python") # here we are storing the new values to a new variable
print(new_data)

Then we would open the file as write now and then just add the new_data variable

with open("practice.txt","w") as f:
    f.write(new_data) # this will overwrite the file with new data
    """

# Practice 3: Search for a string in the file you created.
# opening the file in read mode since we are just searching for a string
with open("practice.txt","r") as f:
    data = f.read() # here we need to read the file first
    if(data.find("learning") != -1): # then use the find function of strings to find the string we are looking for
        print(f"It exists at index {data.find("learning")}.")
    else:
        print("No it doesn't.")

# Practice 4: write a function to find in which line of the file does the word "learning" occur first. Print -1 if word not found
with open("practice.txt","r") as f:
   for data in f:
       line = f.readline()
       print(line)

