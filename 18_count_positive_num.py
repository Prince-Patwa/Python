# Given a list of number, count how maby are positive.

numbers = [1, -2, 3, 4, -5, 6, -7, 8, 9]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

print(f"Positive number count in given list is {positive_number_count}")
