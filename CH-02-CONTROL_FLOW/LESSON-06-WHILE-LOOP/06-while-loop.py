
# ==========================================
# Lesson 06 - While Loop
# Learn Python With Naziya
# ==========================================

# A while loop repeats a block of code as long as the condition is True.

print("========== Example 1 ==========")

count = 1

while count <= 5:
    print(count)
    count += 1

print("\n========== Example 2 ==========")

number = 10

while number >= 1:
    print(number)
    number -= 1

print("\n========== Example 3 ==========")

total = 1

while total <= 5:
    print(f"Square of {total} = {total ** 2}")
    total += 1

print("\n========== Example 4 ==========")

password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Login Successful!")

print("\n========== Example 5 ==========")

sum = 0
i = 1

while i <= 5:
    sum += i
    i += 1

print("Sum =", sum)

print("\n========== End of Lesson ==========")