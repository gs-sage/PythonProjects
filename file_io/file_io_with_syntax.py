"""Using with syntax to open files in python"""

"""IMPORTANT
When using with to open a file, we don't need to close the file,
the with syntax takes care of it automatically.
"""
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("Overwriting the data with the write mode in python.")

with open("demo.txt","r") as f:
    data = f.read()
    print(data)