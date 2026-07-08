# ==========================================
# Lesson 05 - With Statement
# Learn Python With Naziya
# ==========================================

# The 'with' statement automatically
# closes the file after use.

print("========== Example 1 ==========")

with open("sample.txt", "w") as file:
    file.write("Welcome to Learn Python With Naziya!")

print("Data written successfully.")

print("\n========== Example 2 ==========")

with open("sample.txt", "r") as file:
    print(file.read())

print("\n========== Example 3 ==========")

name = input("Enter your name: ")

with open("users.txt", "a") as file:
    file.write(name + "\n")

print("Name saved successfully.")

print("\n========== Example 4 ==========")

with open("users.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n========== Example 5 ==========")

with open("notes.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Using With Statement\n")

print("Notes saved successfully.")

print("\n========== Example 6 ==========")

with open("notes.txt", "r") as file:
    print(file.read())

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file named course.txt
# Store your course name using 'with'
# Read and print the file.