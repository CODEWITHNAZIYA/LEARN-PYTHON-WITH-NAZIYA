
# ==========================================
# Lesson 07 - Break Statement
# Learn Python With Naziya
# ==========================================

# The break statement is used to stop a loop immediately.

print("========== Example 1 ==========")

for number in range(1, 11):
    if number == 6:
        break
    print(number)

print("\n========== Example 2 ==========")

count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1

print("\n========== Example 3 ==========")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    if fruit == "Mango":
        break
    print(fruit)

print("\n========== Example 4 ==========")

while True:
    password = input("Enter Password: ")

    if password == "python123":
        print("Login Successful!")
        break

    print("Incorrect Password. Try Again.")

print("\n========== Example 5 ==========")

for letter in "PYTHON":
    if letter == "H":
        break
    print(letter)

print("\n========== End of Lesson ==========")