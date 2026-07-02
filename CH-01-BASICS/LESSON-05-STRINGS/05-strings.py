
# ==========================================
# Lesson 05 - Strings
# Learn Python With Naziya
# ==========================================

# A string is a sequence of characters.
# Strings are written inside single (' '), double (" "), or triple quotes (""" """)

print("========== Creating Strings ==========")

name = "Naziya"
city = 'Surat'

print("Name :", name)
print("City :", city)

print("\n========== String Indexing ==========")

text = "Python"

print("First Character :", text[0])
print("Second Character :", text[1])
print("Last Character :", text[-1])

print("\n========== String Slicing ==========")

print(text[0:3])
print(text[2:6])
print(text[:4])
print(text[3:])

print("\n========== String Length ==========")

print("Length :", len(text))

print("\n========== String Methods ==========")

message = "learn python"

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())

print("\n========== Replace Method ==========")

sentence = "I love Java"

new_sentence = sentence.replace("Java", "Python")

print(new_sentence)

print("\n========== Find Method ==========")

language = "Python Programming"

print(language.find("Programming"))

print("\n========== Count Method ==========")

word = "banana"

print(word.count("a"))

print("\n========== Membership Operator ==========")

print("P" in text)
print("Java" in text)

print("\n========== Concatenation ==========")

first_name = "Naziya"
last_name = "Shaikh"

full_name = first_name + " " + last_name

print(full_name)

print("\n========== String Formatting ==========")

student = "Ayaan"
marks = 95

print(f"{student} scored {marks} marks.")

print("\n========== Escape Characters ==========")

print("Hello\nWorld")
print("Python\tProgramming")
print("He said, \"Hello\"")