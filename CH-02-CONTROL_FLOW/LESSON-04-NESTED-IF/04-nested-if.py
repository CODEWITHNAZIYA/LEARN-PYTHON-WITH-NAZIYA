
# ==========================================
# Lesson 04 - Nested If
# Learn Python With Naziya
# ==========================================

# A nested if means an if statement inside another if statement.

print("========== Example 1 ==========")

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You are allowed to vote.")
    else:
        print("You need a valid ID.")
else:
    print("You are not eligible to vote.")

print("\n========== Example 2 ==========")

username = "naziya"
password = "python123"

if username == "naziya":
    if password == "python123":
        print("Login Successful!")
    else:
        print("Incorrect Password!")
else:
    print("Invalid Username!")

print("\n========== Example 3 ==========")

marks = 82
attendance = 80

if marks >= 35:
    if attendance >= 75:
        print("Student Passed")
    else:
        print("Attendance is too low.")
else:
    print("Student Failed")

print("\n========== Example 4 ==========")

number = 12

if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is not positive.")

print("\n========== End of Lesson ==========")