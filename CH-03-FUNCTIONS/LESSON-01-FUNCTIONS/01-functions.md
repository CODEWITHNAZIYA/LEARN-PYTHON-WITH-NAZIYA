# Lesson 01 - Functions

## What is a Function?

A **function** is a reusable block of code that performs a specific task.

Functions help us avoid writing the same code again and again.

---

# Why Use Functions?

- Reuse code
- Improve readability
- Reduce repetition
- Make programs easier to maintain

---

# Syntax

```python
def function_name():
    # Code

function_name()
```

---

# Example 1

```python
def greet():
    print("Hello!")

greet()
```

Output

```
Hello!
```

---

# Example 2

```python
def student():
    print("Name: Naziya")

student()
```

Output

```
Name: Naziya
```

---

# How Functions Work

```
Call Function
      │
      ▼
Execute Function
      │
      ▼
Return to Program
```

---

# Important Points

✔ Functions are created using the `def` keyword.

✔ A function runs only when it is called.

✔ One function can be called multiple times.

✔ Function names should be meaningful.

---

# Common Mistakes

❌ Forgetting to call the function.

```python
def greet():
    print("Hello")
```

Nothing will happen until:

```python
greet()
```

---

# Tips

- Use short and meaningful function names.
- Keep one function responsible for one task.
- Avoid writing very long functions.

---

# Summary

In this lesson you learned:

- What is a function?
- Why functions are useful
- Function syntax
- Function calling
- Benefits of functions