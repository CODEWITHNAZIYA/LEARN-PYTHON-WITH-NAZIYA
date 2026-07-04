# ==========================================
# Lesson 02 - Tuples
# Learn Python With Naziya
# ==========================================

# A tuple is used to store multiple items.
# Tuples are ordered and immutable (cannot be changed).

print("========== Example 1 ==========")

fruits = ("Apple", "Banana", "Mango")
print(fruits)

print("\n========== Example 2 ==========")

numbers = (10, 20, 30, 40, 50)
print("First Number :", numbers[0])
print("Last Number  :", numbers[-1])

print("\n========== Example 3 ==========")

colors = ("Red", "Blue", "Green")
for color in colors:
    print(color)

print("\n========== Example 4 ==========")

print("Length of Tuple :", len(colors))

print("\n========== Example 5 ==========")

print("Count of Apple :", fruits.count("Apple"))
print("Index of Mango :", fruits.index("Mango"))

print("\n========== Example 6 ==========")

mixed = ("Naziya", 21, True, 95.5)
print(mixed)

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a tuple of your favorite colors.
# Print the first and last color.
# Print the total number of colors.