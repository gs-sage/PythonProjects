"""Using with syntax to open files in python"""

"""IMPORTANT
When using with to open a file, we don't need to close the file,
the with syntax takes care of it automatically.
"""
with open("demo.txt","r") as f:
    data = f.read()
    print(data)