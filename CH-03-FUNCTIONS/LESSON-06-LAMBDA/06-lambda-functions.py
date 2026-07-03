# ==========================================
# Lesson 06 - Lambda Functions
# Learn Python With Naziya
# ==========================================

# A lambda function is a small anonymous function.
# It is written in a single line.

print("========== Example 1 ==========")

square = lambda number: number ** 2
print("Square of 5 =", square(5))

print("\n========== Example 2 ==========")

add = lambda a, b: a + b
print("Addition =", add(10, 20))

print("\n========== Example 3 ==========")

multiply = lambda x, y: x * y
print("Multiplication =", multiply(4, 6))

print("\n========== Example 4 ==========")

maximum = lambda a, b: a if a > b else b
print("Largest Number =", maximum(25, 40))

print("\n========== Example 5 ==========")

greet = lambda name: f"Welcome, {name}!"
print(greet("Naziya"))

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a lambda function
# that returns the cube of a number.