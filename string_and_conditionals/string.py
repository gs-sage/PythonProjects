first_string = "This is a string."
second_string = 'College name.'
third_string = """This is a third type of string."""

# Concatenation
# This is an example of Concatenation
final_string = first_string + " " + second_string + " " + " " + third_string # adding space in between

print(final_string)

# length of a variable
print(len(first_string))
print(len(final_string)) # len also counts the spaces

# indexing
college_name = "Northeastern University"

ch = college_name[0] # prints N

print(ch)

# IMPORTANT
# cannot change the index value of a string 
# so if we did
# collegeName[0] = "U" # this is not valid, uncomment to try

# print(collegeName) # will give an error, uncomment to try

# Slicing Concept
# Slicing means accessing parts of a string.
# structure is string1[starting_index : ending_index], where ending_index is not included, both index values can be anything to start and end.

print(college_name[0:5]) # prints from 0 index till the 4th index
print(college_name[0:len(college_name)]) # prints the whole things since it starts from 0 index till length of string
print(college_name[0:]) # prints the whole thing since it starts from 0 and even if ending is unspecified, it assumes to take the length of string
print(college_name[3:]) # print as above but prints starting from 3rd index till length of string
print(college_name[:5]) # prints from start till the 4th index
print(college_name[:]) # prints the whole string

# Slicing with Negative index
# Negative index means counting backwards 
""" In normal index counting we go from 0 to whatever the length we want depending on the variable limits. 
In negative index we go backwards so for example in the word apple, the regular index would be:
0:a, 1:p, 2:p, 3:l, 4:e
In backward counting the index would be:
-5:a, -4:p, -3:p, -2:l,-1:e"""

negative_string = "Apple"

print(negative_string[-3:-1]) # will print pl since last index is not included in slicing

# String Functions
a_string = "i am studying python."

# .endswith("string value") function
# returns true if the string ends with the substring we provided.
print(a_string.endswith("on."))

# .capitalize() function
# Capitalizes the first character, only works when specifically called, doesn't change the original string for all occurrences.
print(a_string.capitalize())
print(a_string) # the first letter here won't be capitalized and will print the original value.

# we can set it to be capitalized each time by assigning the variable the capitalized value like
a_string = a_string.capitalize() # now after this the first character will always be capitalized.
print(a_string)

# .replace(oldvalue, newvalue) function
print(a_string.replace("y", "a")) # replaces y with a
print(a_string.replace("python", "java")) # replaces python with java

# .find(word) function
"""finds if the word exists in the string or not
and if it does it returns the first index of the letter that word.
And if the word doesn't exist it will return -1 as conceptually -1 is not real and tries to show out of bounds
of the index. Negative indexes are mostly for slicing function."""
print(a_string.find("am")) # returns 2 since a is in index 2.
print(a_string.find("G")) # returns -1 since it is not in the string and not valid

# .count(word) function
"""Counts the occurence of the substring we provide"""
print(a_string.count("python")) # returns 1 since it only occurs one time in our string variable.
print(a_string.count("java")) # returns 0 since it doesn't exist in our string.