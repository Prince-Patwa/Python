# Determine if a fruit is ripe, overripe, or unripe bassed on its color.(e.g., Banana:Green - Unripe, Yellow - ripe, Brown - Overripe)

fruit = input("Plese enter the fruit name : ").lower()
color = input("Plese enter fruit color : ").lower()

if fruit == "banana":
    if color == "green":
        print("Fruit is Unripe")
    elif color == "yellow":
        print("Fruit is Ripe")
    elif color == "brown":
        print("Fruit is Overripe")
    else:
        print("Sorry, I don't know about this color.")

elif fruit == "apple":
    if color == "green":
        print("Fruit is Unripe")
    elif color == "red":
        print("Fruit is Ripe")
    elif color == "brown":
        print("Fruit is Overripe")
    else:
        print("Sorry, I don't know about this color.")

elif fruit == "mango":
    if color == "green":
        print("Fruit is Unripe")
    elif color == "red":
        print("Fruit is Ripe")
    elif color == "brown":
        print("Fruit is Overripe")
    else:
        print("Sorry, I don't know about this color.")

else:
    print("I don't know about this fruite.")