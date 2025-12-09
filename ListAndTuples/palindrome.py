# program checks if the list contains a palindrome of elements

exampleList = [1,2,3,2,4] # created an example list

print(exampleList) # printed the list for easy debugging

"""We are using the .copy() function here so that we get returned something.
In this case that is the copy of the original list. Just using the .reverse() function
doesn't work as the .reverse() function doesn't return anything to us."""
copyExampleList = exampleList.copy() # used the .copy() function to copy the list
copyExampleList.reverse() # reversed the copied list 
print(copyExampleList) # printed the copied list for debugging

# checking if the original list is equal to the reversed copied list
# if it is then we got a palindrome
if(exampleList == copyExampleList):
    print("The list contains plaindrome of elements.")
else:
    print("The list doesn't contain palindrome of elements.")


"""FYI doing the following doesn't work.
Even though the concept is right, we can't store the .reverse in a 
variable and trying to equal to it also doesn;t work. The variable will store the data but since the 
.reverse function doesn't return anything it won't work so the program will only print the else statement. Uncomment to test in a different file."""

# exampleList.reverse()

# if(exampleList == exampleList.reverse()):
#     print("The list contains plaindrome of elements.")
# else:
#     print("The list doesn't contain palindrome of elements.")