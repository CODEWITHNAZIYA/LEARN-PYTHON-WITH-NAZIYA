
# ==========================================
# Lesson 07 - Keywords
# Learn Python With Naziya
# ==========================================

# Keywords are reserved words in Python.
# We cannot use keywords as variable names.

import keyword

print("========== What are Keywords? ==========")

print("Keywords are reserved words in Python.")
print("They have special meanings.")
print("You cannot use them as variable names.")

print("\n========== Total Keywords ==========")

print("Total Keywords :", len(keyword.kwlist))

print("\n========== List of Python Keywords ==========")

print(keyword.kwlist)

print("\n========== Examples of Keywords ==========")

age = 20

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")

print("\n========== Boolean Keywords ==========")

is_student = True

if is_student:
    print("Student Verified")

print("\n========== Loop Keyword ==========")

for number in range(1, 6):
    print(number)

print("\n========== Function Keyword ==========")

def greet():
    print("Welcome to Learn Python With Naziya!")

greet()

print("\n========== Return Keyword ==========")

def add(a, b):
    return a + b

result = add(10, 20)

print("Addition :", result)

print("\n========== None Keyword ==========")

data = None

print(data)

print("\n========== End of Lesson ==========")