# program to store 9 and 9.0 in a set

# storing 9.0 as a string cause set will take 9.0 as the same as integer 9 if we just keep it as a float
# cause the hash value of integer 9 and float 9.0 is the same in python
store_set = {9,"9.0"} 
print(store_set)

# another possible solution is to use a tuple
store_set1 = {("int", 9), ("float", 9.0)}
print(store_set1)