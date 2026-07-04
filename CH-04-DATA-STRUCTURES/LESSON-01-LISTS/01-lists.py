# ==========================================
# Lesson 01 - Lists
# Learn Python With Naziya
# ==========================================

# A list is used to store multiple items.
# Lists are ordered and mutable (changeable).

print("========== Example 1 ==========")

fruits = ["Apple", "Banana", "Mango"]
print(fruits)

print("\n========== Example 2 ==========")

numbers = [10, 20, 30, 40, 50]
print("First Number :", numbers[0])
print("Last Number  :", numbers[-1])

print("\n========== Example 3 ==========")

students = ["Ali", "Naziya", "Ayaan"]
students.append("Sara")
print(students)

print("\n========== Example 4 ==========")

students.remove("Ali")
print(students)

print("\n========== Example 5 ==========")

colors = ["Red", "Blue", "Green"]
colors[1] = "Yellow"
print(colors)

print("\n========== Example 6 ==========")

for fruit in fruits:
    print(fruit)

print("\n========== Example 7 ==========")

print("Length of Fruits List :", len(fruits))

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a list of your favorite movies.
# Add one movie.
# Remove one movie.
# Print the final list.