
# ==========================================
# Lesson 02 - If Else Statement
# Learn Python With Naziya
# ==========================================

# The if-else statement is used to choose between two conditions.

print("========== Example 1 ==========")

age = 20

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("\n========== Example 2 ==========")

marks = 30

if marks >= 35:
    print("Congratulations! You passed.")
else:
    print("Sorry! You failed.")

print("\n========== Example 3 ==========")

number = -10

if number > 0:
    print("Positive Number")
else:
    print("Negative Number")

print("\n========== Example 4 ==========")

password = input("Enter Password: ")

if password == "python123":
    print("Login Successful!")
else:
    print("Incorrect Password!")

print("\n========== Example 5 ==========")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\n========== End of Lesson ==========")