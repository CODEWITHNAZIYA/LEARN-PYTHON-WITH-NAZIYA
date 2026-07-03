# ==========================================
# Lesson 05 - Keyword Arguments
# Learn Python With Naziya
# ==========================================

# Keyword arguments allow us to pass arguments
# using the parameter names.

print("========== Example 1 ==========")

def student(name, age):
    print("Name :", name)
    print("Age  :", age)

student(name="Naziya", age=21)

print("\n========== Example 2 ==========")

def employee(name, department):
    print("Employee   :", name)
    print("Department :", department)

employee(department="IT", name="Ali")

print("\n========== Example 3 ==========")

def introduce(name, city, country):
    print("Name    :", name)
    print("City    :", city)
    print("Country :", country)

introduce(country="India", city="Surat", name="Naziya")

print("\n========== Example 4 ==========")

def rectangle(length, width):
    area = length * width
    print("Area =", area)

rectangle(width=10, length=5)

print("\n========== Example 5 ==========")

def book(title, author):
    print("Title  :", title)
    print("Author :", author)

book(author="James Clear", title="Atomic Habits")

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a function named profile()
# with three parameters:
# name, city and age.
# Call it using keyword arguments.