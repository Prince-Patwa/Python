# Movie ticket pricing [Problem:- Movie tickets are priced based on age:$12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on wednesday.]

#First method
# age = int(input("Enter age : "))
# day = input("Enter day name (Like : Monday) : ")
# if age < 18:
#     print("Your ticket price is $8")
# else:
#     print("Your ticket price is $12")

# if day == "wednesday" or day == "Wednesday":
#     print("Congratulation today is Wednesday so, you got $2 discount on your ticket.")


# second method
age = int(input("Enter age : "))
day = input("Enter day name (Like : Monday) : ")
day = day.lower()
price = 12 if age >= 18 else 8
if day == "wednesday":
    price = price - 2
print(f"Your ticket price is ${price}")