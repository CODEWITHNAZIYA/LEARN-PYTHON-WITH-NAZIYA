# ==========================================
# Lesson 06 - File Modes
# Learn Python With Naziya
# ==========================================

# Python provides different modes
# to work with files.

print("========== Example 1 ==========")

# Read Mode (r)
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("sample.txt not found.")

print("\n========== Example 2 ==========")

# Write Mode (w)
with open("student.txt", "w") as file:
    file.write("Welcome to Python File Handling!")

print("Data written using write mode.")

print("\n========== Example 3 ==========")

# Append Mode (a)
with open("student.txt", "a") as file:
    file.write("\nLearning File Modes.")

print("Data appended successfully.")

print("\n========== Example 4 ==========")

# Exclusive Create Mode (x)
try:
    with open("new_file.txt", "x") as file:
        file.write("This file is created using x mode.")
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")

print("\n========== Example 5 ==========")

with open("student.txt", "r") as file:
    print(file.read())

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file using x mode.
# Write your name into it.
# Read the file using r mode.