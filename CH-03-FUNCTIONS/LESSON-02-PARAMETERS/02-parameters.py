# ==========================================
# Lesson 02 - Parameters
# Learn Python With Naziya
# ==========================================

# Parameters allow us to pass data to a function.

print("========== Example 1 ==========")

def greet(name):
    print("Hello,", name)

greet("Naziya")

print("\n========== Example 2 ==========")

def student(name, course):
    print("Name :", name)
    print("Course :", course)

student("Naziya", "Python")

print("\n========== Example 3 ==========")

def add(a, b):
    print("Addition =", a + b)

add(10, 20)

print("\n========== Example 4 ==========")

def square(number):
    print("Square =", number ** 2)

square(6)

print("\n========== Example 5 ==========")

def display(city, country):
    print("City :", city)
    print("Country :", country)

display("Surat", "India")

print("\n========== End of Lesson ==========")