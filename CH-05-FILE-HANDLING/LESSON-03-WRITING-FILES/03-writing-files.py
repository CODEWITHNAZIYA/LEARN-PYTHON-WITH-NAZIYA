# ==========================================
# Lesson 03 - Writing Files
# Learn Python With Naziya
# ==========================================

# Writing data into files using Python.

print("========== Example 1 ==========")

file = open("student.txt", "w")
file.write("Name: Naziya\n")
file.write("Course: Python\n")
file.close()

print("Data written successfully.")

print("\n========== Example 2 ==========")

file = open("student.txt", "r")
print(file.read())
file.close()

print("\n========== Example 3 ==========")

file = open("message.txt", "w")
file.write("Welcome to Learn Python With Naziya!")
file.close()

print("Message saved successfully.")

print("\n========== Example 4 ==========")

name = input("Enter your name: ")

file = open("user.txt", "w")
file.write(name)
file.close()

print("User name saved successfully.")

print("\n========== Example 5 ==========")

file = open("user.txt", "r")
print("Stored Name:", file.read())
file.close()

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file named marks.txt
# Store your marks in it.
# Read and print the content.