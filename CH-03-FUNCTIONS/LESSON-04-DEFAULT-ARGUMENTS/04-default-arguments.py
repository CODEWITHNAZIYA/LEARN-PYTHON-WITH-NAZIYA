# ==========================================
# Lesson 04 - Default Arguments
# Learn Python With Naziya
# ==========================================

# Default arguments allow us to use a predefined value
# if no argument is passed.

print("========== Example 1 ==========")

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Naziya")

print("\n========== Example 2 ==========")

def student(name, course="Python"):
    print("Name   :", name)
    print("Course :", course)

student("Naziya")
student("Ali", "Data Science")

print("\n========== Example 3 ==========")

def power(number, exponent=2):
    return number ** exponent

print("Square of 5 :", power(5))
print("Cube of 5   :", power(5, 3))

print("\n========== Example 4 ==========")

def order(item, quantity=1):
    print(f"{quantity} x {item} ordered.")

order("Laptop")
order("Book", 3)

print("\n========== Example 5 ==========")

def employee(name, department="IT"):
    print("Employee   :", name)
    print("Department :", department)

employee("Naziya")
employee("Ayaan", "HR")

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a function named welcome()
# with a default name "Guest".
# Call it with and without an argument.