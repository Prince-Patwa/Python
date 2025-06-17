# Calculate the sum of even numbers up to given number n

number = []
count = int(input("Please enter the number how many number you want to enter: "))
sum_of_even_num = 0

for i in range(count):
    given_number = int(input("Enter a number: "))
    number.append(given_number)

for num in number:
    if num % 2 == 0:
        sum_of_even_num = sum_of_even_num + num

print("The sum of even numbers is:", sum_of_even_num)