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
