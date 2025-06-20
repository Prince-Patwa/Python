# Write a generator function that yields even numbers up to a specified limit.

def even_genrator(limit):
    for i in range(2, limit + 1, 2):
        yield i

number = int(input("Plese enter your limit : "))
for num in even_genrator(number):
    print(num)