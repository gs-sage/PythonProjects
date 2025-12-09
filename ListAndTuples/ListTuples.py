# Practice file for learning List and Tuples

# Lists
marks = [90,100,80,50,65] 
print(marks) # prints the list
print(len(marks)) # prints the length of the list
print(type(marks)) # prints the type of the data type
print(marks[0]) # prints index 0

"""In python Lists unlike other coding languages we can add different data types"""

dataValues = [97.5,100,"John", True] # this is valid in python but wouldn't be in java or c++
print(dataValues) # prints the list without issues
print(type(dataValues)) # will show as class List
print(dataValues[3]) # prints the 3rd index

"""Slicing can also be done in lists"""
print(marks[1:4]) # prints from index 1 to 3
print(marks[:5]) # prints all since last value is not included
print(marks[2:]) # prints from the second index to the last
print(marks[-3:-1]) #prints 80 and 50 since negative index starts from the rightmost index at -1.

# List functions
""".append(value) method adds the value to the end of the list"""
list = [2,1,3] # creating a new list
fruit = ["mango","apple","dragonfruit"] # to see how string list is sorted
list.append(4) # adding 4
print(list)

""".sort() methods sorts the values in ascending order"""
list.sort() # first sort happens
fruit.sort() # first sort happens
print(list)
print(fruit)

""".sort(reverse=True) method reverses the sort"""
list.sort(reverse=True) # first reverse happens
fruit.sort(reverse=True) # first reverse happens
print(list)
print(fruit)

""".reverse() method reverses the list"""
list.reverse() # second reverse happens
fruit.reverse() # second reverse happens
print(list)
print(fruit)

""".insert(index, element) inserts element at a certain index"""
fruit.insert(3, "pineapple") # inserts pineapple at the 3rd index
print(fruit)