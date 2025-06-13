# Swap two numbers using a temporary variable.

firstNo = int(input("Enter first no : "))
secondNo = int(input("Enter second no : "))

temp = firstNo
firstNo = secondNo
secondNo = temp

print("After swapping")
print("First No :",firstNo)
print("Second No :",secondNo)