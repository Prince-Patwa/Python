# Given a string, find the first non-repeated character.

given_string = input("Enter a string: ")
non_repeated_char = ""

for char in given_string:
        if given_string.count(char) == True:    #if given_string.count(char) == True:
                non_repeated_char = char
                break
print("First non-repeated character is:", non_repeated_char)
