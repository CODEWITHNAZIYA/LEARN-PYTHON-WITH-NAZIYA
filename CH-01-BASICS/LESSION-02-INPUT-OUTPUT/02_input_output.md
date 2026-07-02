
# Lesson 02 - Input and Output

## What is Output?

Output means displaying information to the user.

In Python, we use the `print()` function to display output.

Example

```python
print("Hello World")
```

Output

```
Hello World
```

---

# What is Input?

Input means taking information from the user.

In Python, we use the `input()` function.

Example

```python
name = input("Enter your name : ")
```

---

# Output Using Variables

```python
name = "Naziya"

print(name)
```

Output

```
Naziya
```

---

# Taking Input from User

```python
name = input("Enter your name : ")

print(name)
```

---

# Input Always Returns String

Example

```python
age = input("Enter age : ")

print(type(age))
```

Output

```
<class 'str'>
```

---

# Type Casting with Input

Convert string input into integer.

```python
age = int(input("Enter age : "))
```

---

# Simple Example

```python
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(num1 + num2)
```

---

# Common Mistakes

❌ Forgetting type casting

```python
num1 = input("Enter number : ")
num2 = input("Enter number : ")

print(num1 + num2)
```

Output

```
1020
```

✔ Correct

```python
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

print(num1 + num2)
```

Output

```
30
```

---

# Tips

✔ Use `print()` for output.

✔ Use `input()` for user input.

✔ Use type casting when working with numbers.

✔ Always give meaningful input messages.

---

# Summary

In this lesson you learned:

- print()
- input()
- User Input
- Output
- Type Casting
- Simple Programs