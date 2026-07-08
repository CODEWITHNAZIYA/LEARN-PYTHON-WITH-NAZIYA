# ==========================================
# Lesson 07 - Working With Text Files
# Learn Python With Naziya
# ==========================================

print("========== Example 1 ==========")

# Create a text file
with open("notes.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Working with Text Files\n")
    file.write("Practice Every Day\n")

print("Text file created successfully.")

print("\n========== Example 2 ==========")

# Read complete file
with open("notes.txt", "r") as file:
    print(file.read())

print("\n========== Example 3 ==========")

# Append new data
with open("notes.txt", "a") as file:
    file.write("Keep Learning Python\n")

print("New line added successfully.")

print("\n========== Example 4 ==========")

# Read line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n========== Example 5 ==========")

# Count total lines
with open("notes.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))

print("\n========== Example 6 ==========")

# Count total words
with open("notes.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total Words:", len(words))

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file named diary.txt
# Write three lines.
# Append one new line.
# Read the file.
# Count total lines.