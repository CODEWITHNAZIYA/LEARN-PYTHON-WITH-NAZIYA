
# ==========================================
# Lesson 09 - Pass Statement
# Learn Python With Naziya
# ==========================================

# The pass statement is a placeholder.
# It does nothing and is used when code will be added later.

print("========== Example 1 ==========")

number = 10

if number > 5:
    pass

print("Program executed successfully.")

print("\n========== Example 2 ==========")

age = 20

if age >= 18:
    pass
else:
    print("Not Eligible")

print("Checking completed.")

print("\n========== Example 3 ==========")

for i in range(5):
    if i == 3:
        pass
    print(i)

print("\n========== Example 4 ==========")

count = 1

while count <= 3:
    pass
    print(count)
    count += 1

print("\n========== Example 5 ==========")

def greet():
    pass

print("Function created successfully.")

print("\n========== End of Lesson ==========")