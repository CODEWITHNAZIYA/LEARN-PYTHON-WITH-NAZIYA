# ==========================================
# Lesson 04 - Dictionaries
# Learn Python With Naziya
# ==========================================

# A dictionary stores data in key-value pairs.

print("========== Example 1 ==========")

student = {
    "name": "Naziya",
    "age": 21,
    "course": "Python"
}

print(student)

print("\n========== Example 2 ==========")

print("Name :", student["name"])
print("Course :", student["course"])

print("\n========== Example 3 ==========")

student["city"] = "Surat"
print(student)

print("\n========== Example 4 ==========")

student["age"] = 22
print(student)

print("\n========== Example 5 ==========")

student.pop("course")
print(student)

print("\n========== Example 6 ==========")

for key, value in student.items():
    print(key, ":", value)

print("\n========== Example 7 ==========")

print("Keys :", student.keys())
print("Values :", student.values())

print("\n========== Example 8 ==========")

print("Total Items :", len(student))

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a dictionary for a book.
# Store title, author and price.
# Print all key-value pairs.