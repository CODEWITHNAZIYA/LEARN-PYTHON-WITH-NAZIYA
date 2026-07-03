# ==========================================
# Lesson 07 - Recursion
# Learn Python With Naziya
# ==========================================

# Recursion is a technique where a function
# calls itself until a condition is met.

print("========== Example 1 ==========")

def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)

countdown(5)

print("\n========== Example 2 ==========")

def print_numbers(number):
    if number == 6:
        return

    print(number)
    print_numbers(number + 1)

print_numbers(1)

print("\n========== Example 3 ==========")

def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)

print("Factorial of 5 =", factorial(5))

print("\n========== Example 4 ==========")

def sum_numbers(number):
    if number == 1:
        return 1

    return number + sum_numbers(number - 1)

print("Sum =", sum_numbers(5))

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a recursive function
# to print numbers from 10 to 1.