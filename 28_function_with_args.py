# Write a function that takes variable number of arguments and returns their sum.

def sum_args(*args):
    return sum(args)

print(sum_args(1,2,3))
print(sum_args(1,2,3,4))