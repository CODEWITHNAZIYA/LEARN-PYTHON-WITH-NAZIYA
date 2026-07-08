# ==========================================
# Lesson 01 - File Basics
# Learn Python With Naziya
# ==========================================

# File handling allows us to create, read,
# write, and manage files in Python.

print("========== Example 1 ==========")

# Creating a file
file = open("sample.txt", "w")
file.write("Welcome to Learn Python With Naziya!")
file.close()

print("File created successfully.")

print("\n========== Example 2 ==========")

# Reading a file
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

print("\n========== Example 3 ==========")

# Checking file exists by opening it
try:
    file = open("sample.txt", "r")
    print("File opened successfully.")
    file.close()

except FileNotFoundError:
    print("File not found.")

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file called student.txt
# Write your name into it.
# Read the file and print its content.