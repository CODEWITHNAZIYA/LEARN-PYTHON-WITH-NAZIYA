# ==========================================
# Lesson 03 - Return Statement
# Learn Python With Naziya
# ==========================================

# The return statement sends a value back from a function.

print("========== Example 1 ==========")

def greet():
    return "Hello, Welcome to Python!"

message = greet()
print(message)

print("\n========== Example 2 ==========")

def add(a, b):
    return a + b

result = add(10, 20)
print("Addition =", result)

print("\n========== Example 3 ==========")

def square(number):
    return number ** 2

print("Square =", square(6))

print("\n========== Example 4 ==========")

def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Naziya", "Shaikh"))

print("\n========== Example 5 ==========")

def is_even(number):
    return number % 2 == 0

print(is_even(8))
print(is_even(7))

print("\n========== End of Lesson ==========")