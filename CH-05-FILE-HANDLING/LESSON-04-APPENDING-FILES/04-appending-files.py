# ==========================================
# Lesson 04 - Appending Files
# Learn Python With Naziya
# ==========================================

# Appending means adding new data
# without deleting existing content.

print("========== Example 1 ==========")

file = open("notes.txt", "a")
file.write("Python is fun to learn.\n")
file.close()

print("Data appended successfully.")

print("\n========== Example 2 ==========")

file = open("notes.txt", "r")
print(file.read())
file.close()

print("\n========== Example 3 ==========")

note = input("Enter a new note: ")

file = open("notes.txt", "a")
file.write(note + "\n")
file.close()

print("Your note has been saved.")

print("\n========== Example 4 ==========")

file = open("notes.txt", "r")

for line in file:
    print(line.strip())

file.close()

print("\n========== Example 5 ==========")

file = open("students.txt", "a")
file.write("Naziya\n")
file.write("Ali\n")
file.write("Sara\n")
file.close()

print("Student names saved.")

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file named diary.txt
# Add three diary entries using append mode.
# Read and display the file.