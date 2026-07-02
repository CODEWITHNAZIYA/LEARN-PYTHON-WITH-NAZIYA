
# ==========================================
# Lesson 03 - Elif Statement
# Learn Python With Naziya
# ==========================================

# The elif statement is used to check multiple conditions.

print("========== Example 1 ==========")

marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 35:
    print("Grade: C")
else:
    print("Fail")

print("\n========== Example 2 ==========")

number = 0

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

print("\n========== Example 3 ==========")

day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")

print("\n========== Example 4 ==========")

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

print("\n========== End of Lesson ==========")