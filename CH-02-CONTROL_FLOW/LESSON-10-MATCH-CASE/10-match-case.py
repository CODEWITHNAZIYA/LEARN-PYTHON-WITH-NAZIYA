
# ==========================================
# Lesson 10 - Match Case
# Learn Python With Naziya
# ==========================================

# Match Case is available in Python 3.10 and above.
# It is used as an alternative to multiple if-elif statements.

print("========== Example 1 ==========")

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")

print("\n========== Example 2 ==========")

fruit = "Apple"

match fruit:
    case "Apple":
        print("Red Fruit")
    case "Banana":
        print("Yellow Fruit")
    case "Mango":
        print("King of Fruits")
    case _:
        print("Unknown Fruit")

print("\n========== Example 3 ==========")

operation = "+"

a = 10
b = 5

match operation:
    case "+":
        print("Addition =", a + b)
    case "-":
        print("Subtraction =", a - b)
    case "*":
        print("Multiplication =", a * b)
    case "/":
        print("Division =", a / b)
    case _:
        print("Invalid Operation")

print("\n========== Example 4 ==========")

grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Average")
    case _:
        print("Invalid Grade")

print("\n========== End of Lesson ==========")