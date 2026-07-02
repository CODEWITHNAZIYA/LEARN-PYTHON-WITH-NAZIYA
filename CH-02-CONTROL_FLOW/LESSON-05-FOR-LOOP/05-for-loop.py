
# ==========================================
# Lesson 05 - For Loop
# Learn Python With Naziya
# ==========================================

# A for loop is used to repeat a block of code.

print("========== Example 1 ==========")

for i in range(5):
    print(i)

print("\n========== Example 2 ==========")

for number in range(1, 6):
    print(number)

print("\n========== Example 3 ==========")

for number in range(2, 11, 2):
    print(number)

print("\n========== Example 4 ==========")

name = "Python"

for letter in name:
    print(letter)

print("\n========== Example 5 ==========")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

print("\n========== Example 6 ==========")

for i in range(1, 6):
    print(f"Square of {i} = {i ** 2}")

print("\n========== Example 7 ==========")

total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)

print("\n========== End of Lesson ==========")