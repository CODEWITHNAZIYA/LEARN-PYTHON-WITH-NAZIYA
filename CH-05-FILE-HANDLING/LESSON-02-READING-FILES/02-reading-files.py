# ==========================================
# Lesson 02 - Reading Files
# Learn Python With Naziya
# ==========================================

# Before running this program,
# make sure sample.txt exists.

print("========== Example 1 ==========")

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

print("\n========== Example 2 ==========")

file = open("sample.txt", "r")
first_line = file.readline()
print(first_line)
file.close()

print("\n========== Example 3 ==========")

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()

print("\n========== Example 4 ==========")

file = open("sample.txt", "r")
lines = file.readlines()

print(lines)

file.close()

print("\n========== Example 5 ==========")

try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found!")

print("\n========== End of Lesson ==========")

# ==========================
# Mini Challenge
# ==========================
# Create a file named notes.txt
# Read all its contents
# Print each line separately.