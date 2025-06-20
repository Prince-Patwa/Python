# Compute the factorial of a number using a while loop.

number = int(input("Please enter a number to calculate the factorial: "))
calculated_factorial = 1

while number >= 1:
    calculated_factorial *= number    # calculated_factorial = calculated_factorial * number
    number -= 1     # number = number - 1
print(f"Calculated factorial of given number is : {calculated_factorial}")