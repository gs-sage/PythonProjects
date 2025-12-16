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

# Practice 3: Search for a string in the file you created.
# opening the file in read mode since we are just searching for a string
with open("practice.txt","r") as f:
    data = f.read() # here we need to read the file first
    if(data.find("learning") != -1): # then use the find function of strings to find the string we are looking for
        print(f"It exists at index {data.find("learning")}.")
    else:
        print("No it doesn't.")

# Practice 4: function to find which line the word above exists.
def check_for_line():
    word = "learning"
    line_count = 1 # cause line starts at 1
    data = True # creating a true state for data so once the lines are over it becomes false
    with open("practice.txt","r") as f:
        while data: # data stays true till it has lines with values, once an empty line comes it becomes false
            data = f.readline()
            if(word in data):
                print(f"{word} found at line {line_count}.")
                break
            # else:
            #     print("Word not found") # will print for first line since the file only has the word on line 2, uncomment to confirm

            line_count+=1

check_for_line() # calling the function
