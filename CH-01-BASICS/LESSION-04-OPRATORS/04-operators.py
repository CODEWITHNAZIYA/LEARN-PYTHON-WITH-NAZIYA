# ==========================================
# Lesson 04 - Operators
# Learn Python With Naziya
# ==========================================

# Operators are used to perform different operations on variables and values.

print("========== Arithmetic Operators ==========")

a = 20
b = 5

print("Value of a =", a)
print("Value of b =", b)

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponent :", a ** b)

print("\n========== Comparison Operators ==========")

x = 10
y = 15

print("x == y :", x == y)
print("x != y :", x != y)
print("x > y :", x > y)
print("x < y :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

print("\n========== Assignment Operators ==========")

num = 10

print("Original Value :", num)

num += 5
print("After += :", num)

num -= 2
print("After -= :", num)

num *= 3
print("After *= :", num)

num /= 2
print("After /= :", num)

print("\n========== Logical Operators ==========")

age = 20
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or False)
print(not has_id)

print("\n========== Membership Operators ==========")

name = "Naziya"

print("N" in name)
print("z" in name)
print("A" not in name)

print("\n========== Identity Operators ==========")

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print(list1 is list2)
print(list1 is list3)

print(list1 == list3)