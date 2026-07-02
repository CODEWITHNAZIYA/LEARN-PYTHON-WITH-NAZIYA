
# ==========================================================
# Project Name : Student Information System
# Chapter 1 Mini Project
# Learn Python With Naziya
# ==========================================================

print("=" * 50)
print("      STUDENT INFORMATION SYSTEM")
print("=" * 50)

# Taking input from the user

name = input("Enter Student Name : ")
age = int(input("Enter Age : "))
city = input("Enter City : ")
course = input("Enter Course : ")

python_marks = int(input("Python Marks : "))
math_marks = int(input("Math Marks : "))
english_marks = int(input("English Marks : "))

# Calculation

total = python_marks + math_marks + english_marks
percentage = total / 3

# Display Result

print("\n")
print("=" * 50)
print("         STUDENT REPORT")
print("=" * 50)

print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"City        : {city}")
print(f"Course      : {course}")

print("-" * 50)

print(f"Python      : {python_marks}")
print(f"Math        : {math_marks}")
print(f"English     : {english_marks}")

print("-" * 50)

print(f"Total Marks : {total}")
print(f"Percentage  : {percentage:.2f}%")

print("-" * 50)

if percentage >= 35:
    print("Result      : PASS 🎉")
else:
    print("Result      : FAIL")

print("=" * 50)
print("Thank You!")
print("=" * 50)