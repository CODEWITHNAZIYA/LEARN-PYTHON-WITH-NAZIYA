
# ==========================================
# Lesson 08 - Continue Statement
# Learn Python With Naziya
# ==========================================

# The continue statement skips the current iteration
# and moves to the next iteration.

print("========== Example 1 ==========")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

print("\n========== Example 2 ==========")

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)

print("\n========== Example 3 ==========")

word = "PYTHON"

for letter in word:

    if letter == "T":
        continue

    print(letter)

print("\n========== Example 4 ==========")

count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)

print("\n========== Example 5 ==========")

for number in range(1, 11):

    if number % 3 == 0:
        continue

    print(number)

print("\n========== End of Lesson ==========")