# ==========================================
# Lesson 03 - Sets
# Learn Python With Naziya
# ==========================================

# A set is used to store multiple unique items.
# Sets are unordered and do not allow duplicate values.

print("========== Example 1 ==========")

fruits = {"Apple", "Banana", "Mango"}
print(fruits)

print("\n========== Example 2 ==========")

numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

print("\n========== Example 3 ==========")

colors = {"Red", "Blue", "Green"}
colors.remove("Blue")
print(colors)

print("\n========== Example 4 ==========")

cities = {"Surat", "Mumbai", "Delhi"}
for city in cities:
    print(city)

print("\n========== Example 5 ==========")

A = {1, 2, 3}
B = {3, 4, 5}

print("Union :", A.union(B))
print("Intersection :", A.intersection(B))
print("Difference :", A.difference(B))

print("\n========== Example 6 ==========")

students = {"Ali", "Naziya", "Ali", "Sara"}
print(students)

print("\n========== Example 7 ==========")

print("Length of Set :", len(students))

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create two sets of your favorite fruits.
# Print their union and intersection.