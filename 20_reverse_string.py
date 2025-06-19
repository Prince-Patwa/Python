# Reverse a string using a loop.

int_string = input("Enter a string : ")
reversed_string = ""

for char in int_string:
    reversed_string = char + int_string
print("Reverse string is :", reversed_string)
