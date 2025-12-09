# This program finds the number of occurrences of a character or word in a string

user_input = input("Type a sentence:\n")
print()

print("Type a word or character for the program to find.")
print("It will return the number of times it occurs.")

print()

word_find = input("Word/Character to find: ")
print(f"The word {word_find} occurs {user_input.count(word_find)} times.")