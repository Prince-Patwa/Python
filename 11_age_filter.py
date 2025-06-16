# Age group categorization [Classify a person's age group: Child(< 13), Teenager(13-19), Adult(20_59), Senior(60+)]

age = int(input("Enter your age : "))

if age < 13:
    print("Your are child.")
elif age >= 13 and age <= 19:
    print("You are teenager.")
elif age >= 20 and age <= 59:
    print("You are adult.")
else:
    print("You are senior.")
