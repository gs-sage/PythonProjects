# program that just has a basic dictionary and prints it to terminal

word_meaning = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal",
}

print(word_meaning) # prints the dictionary
print(word_meaning.get("table")) # prints the value of table key
print(word_meaning["table"][0]) # prints the first index value of table
print(word_meaning.get("table")[1]) # prints the second index value of table
print(word_meaning.keys()) # gets the keys in the dictionary
print(word_meaning.items()) # gets the key:value in the dictionary
print(word_meaning.values()) # gets the value in the dictionary
word_meaning.update({"apple":"a fruit"}) # adds a new key and value to the dictionary
print(word_meaning)