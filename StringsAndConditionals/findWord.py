# This program finds the number of occurrences of a character or word in a string

userInput = input("Type a sentence:\n")
print()

print("Type a word or character for the program to find.")
print("It will return the number of times it occurs.")

print()

wordFind = input("Word/Character to find: ")
print(f"The word {wordFind} occurs {userInput.count(wordFind)} times.")