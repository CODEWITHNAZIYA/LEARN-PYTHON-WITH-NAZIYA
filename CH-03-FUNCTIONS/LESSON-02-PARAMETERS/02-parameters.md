# Lesson 02 - Parameters

## What are Parameters?

A **parameter** is a variable written inside the parentheses of a function definition.

Parameters allow us to pass data into a function.

---

# Why Use Parameters?

- Make functions reusable.
- Pass different values.
- Avoid hardcoding values.
- Make code flexible.

---

# Syntax

```python
def function_name(parameter):
    # Code

function_name(value)
```

---

# Example 1

```python
def greet(name):
    print("Hello", name)

greet("Naziya")
```

Output

```
Hello Naziya
```

---

# Example 2

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output

```
30
```

---

# Multiple Parameters

```python
def student(name, course):
    print(name)
    print(course)

student("Naziya", "Python")
```

---

# How Parameters Work

```
Function Call
      │
      ▼
Values Passed
      │
      ▼
Parameters Receive Values
      │
      ▼
Function Executes
```

---

# Parameter vs Argument

| Parameter | Argument |
|------------|----------|
| Variable inside function | Actual value passed to function |
| Written in function definition | Written in function call |

Example

```python
def greet(name):      # name → Parameter
    print(name)

greet("Naziya")       # "Naziya" → Argument
```

---

# Important Points

✔ Parameters are written in the function definition.

✔ Arguments are passed while calling the function.

✔ A function can have one or more parameters.

✔ Parameter names should be meaningful.

---

# Common Mistakes

❌ Missing argument

```python
def greet(name):
    print(name)

greet()
```

This produces a **TypeError**.

---

✔ Correct

```python
greet("Naziya")
```

---

# Tips

- Use descriptive parameter names.
- Pass the correct number of arguments.
- Keep functions simple.

---

# Summary

In this lesson you learned:

- What are parameters?
- Parameters vs arguments
- Single parameter
- Multiple parameters
- Common mistakes