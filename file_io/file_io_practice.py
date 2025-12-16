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
    word = "little"
    line_count = 1 # cause line starts at 1
    data = True # creating a true state for data so once the lines are over it becomes false
    with open("practice.txt","r") as f:
        while data: # data stays true till it has lines with values, once an empty line comes it becomes false
            data = f.readline()
            if(word in data):
                print(f"{word} found at line {line_count}.")
                return
            # else:
            #     print("Word not found") # will print for first line since the file only has the word on line 2, uncomment to confirm

            line_count+=1
    print("Word not found.") # this will only print once if the word is not found

check_for_line() # calling the function

# Practice 5: from a file containing numbers separated by comma, print the count of even numbers
with open("numbers.txt","r") as f:
    data = f.read()
    print(data)

    # one way to do this problem, not the best cause it won't include the last number in the file since it doesn't have an comma at the end
    # num = "" # creating an empty string to add values later
    # for i in range(len(data)): 
    #     if(data[i] == ","):
    #         print(num)
    #         num = "" # we need to initialize the num as empty string again so it doesn't keep printing previous values.
    #     else:
    #         num+=data[i] # each time the comma has not been found, add the value of string to the num variable

    # Another way to do this using the split command
    nums = data.split(",")
    print(nums)
    # nums = int(nums) # we can't do this cause nums is a list and not an individual string value
    count = 0
    for val in nums:
        #print(val) # now val here we can convert to integer since it takes individual values from the list
        if(int(val)%2==0):
            print(val)
            count+=1
    print(count)
