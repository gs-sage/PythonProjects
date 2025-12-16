"""Deleting a file
Using the os module
Module is a file written by another programmer that generally
has functions we can use."""

"""IMPORTANT
To use a module we have to import it first. For example, to use the delete function, we import the os module

import os
os.remove("filename")"""

# importing required libraries
import os

# create file, if it doesn't exist
# The following line will then remove the file.
os.remove("sample.txt") 

