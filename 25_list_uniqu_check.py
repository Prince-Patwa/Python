# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

#first method
# item = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set(item)
# print(unique_item)


# second method
items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in unique_item:
        print(f"Duplicate item is : {item}")
        break
    else:
        unique_item.add(item)
print(unique_item)