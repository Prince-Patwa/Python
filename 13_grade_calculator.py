# Assign a letter grade based on a student's score : A(90-100), B(80-89), C(70-79), D(60-69), F(below 60).

#First method
# score = int(input("Plese enter your score : "))
# if score >= 90 and score <= 100:
#     print("Excellent,👌 your grade is A")
# elif score >= 80 and score <= 89:
#     print("Very Very Good,👍 your grade is B")
# elif score >= 70 and score <= 79:
#     print("Very Good, 👍 your grade is C")
# elif score >= 60 and score <= 69:
#     print("Good, 👍 your grade is D")
# elif score < 60:
#     print("Sorry,😔 you are fail.")
# else:
#     print("You enter the score above the 100.\nPlese enter your score below the 100.")


# Second Method
score = int(input("Plese enter your score : "))
if score >= 101:
    print("You enter the score above the 100.\nPlese enter your score below the 100.")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade {grade}")