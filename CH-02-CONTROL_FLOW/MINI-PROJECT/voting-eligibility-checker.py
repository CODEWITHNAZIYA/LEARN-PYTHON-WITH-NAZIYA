
# ==========================================
# Mini Project - Voting Eligibility Checker
# Learn Python With Naziya
# ==========================================

print("=" * 40)
print("      Voting Eligibility Checker")
print("=" * 40)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

print("\nChecking eligibility...\n")

if country.lower() == "india":
    if age >= 18:
        print("Congratulations,", name + "!")
        print("You are eligible to vote.")
    else:
        print("Sorry,", name + ".")
        print("You are not eligible to vote.")
        print("You can vote after", 18 - age, "year(s).")
else:
    print("This program currently supports Indian voters only.")

print("\nThank you for using this program!")