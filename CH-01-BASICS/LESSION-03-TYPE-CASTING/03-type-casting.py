
# ==========================================
# Lesson 03 - Type Casting
# Learn Python With Naziya
# ==========================================

print("========== What is Type Casting? ==========")

# Type casting means converting one data type into another.

number = "100"

print("Before Type Casting")
print(number)
print(type(number))

print("\nAfter Type Casting")

number = int(number)

print(number)
print(type(number))

print("\n========== String to Float ==========")

price = "99.99"

print("Before :", type(price))

price = float(price)

print("After :", type(price))
print(price)

print("\n========== Integer to String ==========")

age = 21

print("Before :", type(age))

age = str(age)

print("After :", type(age))
print(age)

print("\n========== Float to Integer ==========")

height = 5.9

print("Before :", height)

height = int(height)

print("After :", height)

print("\n========== Integer to Float ==========")

marks = 85

print(type(marks))

marks = float(marks)

print(type(marks))
print(marks)

print("\n========== Boolean Type Casting ==========")

print(bool(1))
print(bool(0))
print(bool("Python"))
print(bool(""))

print("\n========== Type Casting with User Input ==========")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Addition =", num1 + num2)

print("\n========== End of Lesson ==========")