"""Dictionaries are used to store data values in key:value pairs.
They are unordered, mutable(changeable) and don't allow duplicate keys."""

# Keys in dictionary cannot be lists or dictionaries
# Value in dictionary can be any value
dict = {
    "key":"value",
    "name":"Gaurav",
    "learning":"coding",
    "age":30,
    "is_adult":True,
    "marks":94.4,
    "subjects":["python","C","Java"],
    "topics":("dict","set"),
}

print(dict)
print(type(dict))

# To access values in a dictionary we use the key
# print(dict["key"])
print(dict["key"])
print(dict["name"])
print(dict["is_adult"])

# we can also assign new value to the keys in a dictionary
dict["name"] = "Gaurav Saymi"
print(dict["name"])

# we can also add something to the dictionary
dict["enjoys"] = "food" # gets added to the end of the dictionary
print(dict)

# we can also create an empty dictionary
null_dict = {}
print(null_dict)
null_dict["name"] = "Null Dictionary"
print(null_dict)

# Nested Dictionary
# this happens by making the value of a key a dictionary itself
# example of nested dictionary
student = {
    "name":"John",
    "subjects":{
        "Physics":97,
        "Chemistry":98,
        "Math":99
    }
}
print(student) # printing the nested dictionary

# we can also get the values of the nested dictionary as needed
print(student["subjects"]["Chemistry"]) # gives output 98

# Dictionary Methods

""".keys() method returns all keys in a dictionary"""
print(student.keys()) # won't print the keys of the nested dictionary. Only prints the outer keys
print(len(student)) # prints the total of the key:value pairs in the dictionary
print(len(list(student.keys()))) # or we can use this to get the total keys in dictionary

""".values() method returns the collection of all the values in a dictionary"""
print(dict.values())
print(len(dict.values())) # not necessary to convert to list to get the count
print(student.values())
print(len(student.values())) # not necessary to convert to list to get the count

""".items() method returns all key:value pairs as tuples"""
print(student.items())
# we can also access these tuples individually
pairs = list(student.items()) # converting to list so it doesn't print dict_items in output
print(pairs[0])

""".get("key") method returns value of the key we pass"""
# The difference between using .get() and the usual normal way of calling a dictionary key
# is that if we call a key that doesn't exist, the normal way will give an error while
# using the .get() method returns a value of None
print(dict.get("name"))
print(student["name"])
print(student.get("name2")) # returns None, no error seen
# print(student["name2"]) # gives error, uncomment line to see

""".update() method, we can pass any additonal or new dictionary and it adds to our dictionary"""
student.update({"city":"Tulsa"}) # can pass with key:values
print(student)

new_dict = {"state":"ok"}
student.update(new_dict) # or can pass a dictionary that has the values
print(student) # we can see the new values added to the end of the dictionary


"""Set is the collection of the unordered items. Each element
in the set must be unique and immutable."""
# List and dictionaries can't be stored inside sets cause these have mutable(changeable) values.
"""IMPORTANT: Set is mutable but the elements inside sets are immutable."""
collection = {1,2,3,4}

print(collection)
print(type(collection))

# if we create a new set with repeating values it will only print the distinct items and ignore duplicate values.
new_collection = {1,2,2,2,"hello","world","world"}
print(new_collection)

# set doesn't follow any order
# if we make a new collection again using the same values and add something it can print out values in completely different order.
new_collection2 = {1,2,2,2,"hello","world","world",4}
print(new_collection2) # output will be different in order

# using len function on set also only prints the count of unique elements and ignores duplicates
print(len(new_collection2))

# creating an empty set
empty_set = set() # syntax for empty set
print(type(empty_set))

# Set Methods

""".add() method adds an element to the set"""
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
empty_set.add(4)
empty_set.add(2)
empty_set.add((1,2,3))
empty_set.add("Yello")
print(empty_set) # prints the unique value in set

""".remove() method removes an element from the set"""
empty_set.remove(2)
print(empty_set) # will only show unique value after something is removed from set

# if we try to remove a value that doesn't exist it gives an error
# empty_set.remove(6) # gives an error, uncomment to check

""".clear() method empties the set"""
print(len(empty_set))
empty_set.clear() # clears all values from set
print(empty_set)
print(len(empty_set)) # len will be 0 after clearing the set

""".pop() removes a random value from the set"""
collections = {"hello","college","world","coding","python"}
print(collections.pop()) # removes a random value and prints the value to output

# IMPORTANT Set Methods

""".union(set2) method combines both set values and returns new set with unique values, ignores duplicates"""
union_collection = collections.union(collection)
print(union_collection) 

""".intersection(set2) combines common values and returns new set"""
intersection_collection = new_collection2.intersection(collections)
print(intersection_collection)

