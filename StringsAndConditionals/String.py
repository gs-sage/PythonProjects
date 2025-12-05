firstString = "This is a string."
secondString = 'College name.'
thirdString = """This is a third type of string."""

# Concatenation
# This is an example of Concatenation
finalString = firstString + " " + secondString + " " + " " + thirdString # adding space in between

print(finalString)

# length of a variable
print(len(firstString))
print(len(finalString)) # len also counts the spaces

# indexing
collegeName = "Northeastern University"

ch = collegeName[0] # prints N

print(ch)

# IMPORTANT
# cannot change the index value of a string 
# so if we did
# collegeName[0] = "U" # this is not valid, uncomment to try

# print(collegeName) # will give an error, uncomment to try

# Slicing Concept
# Slicing means accessing parts of a string.
# structure is string1[starting_index : ending_index], where ending_index is not included, both index values can be anything to start and end.

print(collegeName[0:5]) # prints from 0 index till the 4th index
print(collegeName[0:len(collegeName)]) # prints the whole things since it starts from 0 index till length of string
print(collegeName[0:]) # prints the whole thing since it starts from 0 and even if ending is unspecified, it assumes to take the length of string
print(collegeName[3:]) # print as above but prints starting from 3rd index till length of string
print(collegeName[:5]) # prints from start till the 4th index
print(collegeName[:]) # prints the whole string

# Slicing with Negative index
# Negative index means counting backwards 
""" In normal index counting we go from 0 to whatever the length we want depending on the variable limits. 
In negative index we go backwards so for example in the word apple, the regular index would be:
0:a, 1:p, 2:p, 3:l, 4:e
In backward counting the index would be:
-5:a, -4:p, -3:p, -2:l,-1:e"""

negString = "Apple"

print(negString[-3:-1]) # will print pl since last index is not included in slicing

# String Functions
aString = "i am studying python."

# .endswith("string value") function
# returns true if the string ends with the substring we provided.
print(aString.endswith("on."))

# .capitalize() function
# Capitalizes the first character, only works when specifically called, doesn't change the original string for all occurrences.
print(aString.capitalize())
print(aString) # the first letter here won't be capitalized and will print the original value.

# we can set it to be capitalized each time by assigning the variable the capitalized value like
aString = aString.capitalize() # now after this the first character will always be capitalized.
print(aString)

# .replace(oldvalue, newvalue) function
print(aString.replace("y", "a")) # replaces y with a
print(aString.replace("python", "java")) # replaces python with java

# .find(word) function
"""finds if the word exists in the string or not
and if it does it returns the first index of the letter that word.
And if the word doesn't exist it will return -1 as conceptually -1 is not real and tries to show out of bounds
of the index. Negative indexes are mostly for slicing function."""
print(aString.find("am")) # returns 2 since a is in index 2.
print(aString.find("G")) # returns -1 since it is not in the string and not valid

# .count(word) function
"""Counts the occurence of the substring we provide"""
print(aString.count("python")) # returns 1 since it only occurs one time in our string variable.
print(aString.count("java")) # returns 0 since it doesn't exist in our string.