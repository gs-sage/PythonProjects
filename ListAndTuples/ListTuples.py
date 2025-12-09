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

""".remove(value) method removes the first occurrence of the value you provide"""
fruit.insert(0, "pineapple")
print(fruit) # will have two pineapple
fruit.remove("pineapple")
print(fruit) # should only have one after the .remove() method removes the first occurrence of pineapple

""".pop(index) method removes particular value at an index"""
fruit.pop(1)
print(fruit)


"""===Tuples==="""
"""built in data type that lets us create immutable sequence of values"""
tup = (2,1,3,1)
print(type(tup))
print(tup[0])
# tup[0] = 5 # this is not allowed in tuples, and will throw an error, uncomment to try.
print(tup[1:3]) # can also use slicing in tuples

# can also create an empty tuple
tup1 = ()
print(tup1)
print(type(tup1))

tup2 = (1,) # need to keep comma to let python know this is a tuple, otherwise it will take the values as different type
print(tup2)
print(type(tup2))

# Tuple functions
""".index(element) method finds the first index occurence of the element"""
print(tup.index(3)) # will give index 2 as output

""".count(element) method counts the total occurrences of the element in the tuple"""
print(tup.count(1)) # will give 2 output