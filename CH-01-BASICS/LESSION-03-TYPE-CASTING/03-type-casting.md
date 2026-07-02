
# Lesson 03 - Type Casting

## What is Type Casting?

Type Casting means converting one data type into another.

Python provides built-in functions for type conversion.

---

# Why Do We Use Type Casting?

Sometimes user input or data is not in the required format.

Type casting helps convert it into the correct data type.

---

# Common Type Casting Functions

| Function | Converts To |
|----------|-------------|
| int() | Integer |
| float() | Float |
| str() | String |
| bool() | Boolean |

---

# String to Integer

Example

```python
number = "100"

number = int(number)

print(number)
```

Output

```
100
```

---

# Integer to String

```python
age = 21

age = str(age)

print(age)
```

---

# String to Float

```python
price = "99.99"

price = float(price)
```

---

# Float to Integer

```python
height = 5.8

height = int(height)
```

Output

```
5
```

**Note:** The decimal part is removed.

---

# Boolean Type Casting

```python
print(bool(1))
print(bool(0))
```

Output

```
True
False
```

---

# Type Casting with User Input

```python
age = int(input("Enter your age : "))
```

Without `int()`, the input is stored as a string.

---

# Common Mistakes

❌ Wrong

```python
num1 = input("Enter Number : ")
num2 = input("Enter Number : ")

print(num1 + num2)
```

Output

```
1020
```

✔ Correct

```python
num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

print(num1 + num2)
```

Output

```
30
```

---

# Tips

- Use `int()` for whole numbers.
- Use `float()` for decimal numbers.
- Use `str()` to convert numbers into text.
- Always use type casting with numeric user input.

---

# Summary

In this lesson you learned:

- What is Type Casting?
- int()
- float()
- str()
- bool()
- Type Casting with input()