# Lesson 07 - Recursion

## What is Recursion?

**Recursion** is a programming technique where a function calls itself to solve a problem.

The function keeps calling itself until a **base case** is reached.

---

# Why Use Recursion?

- Solve repetitive problems.
- Make some algorithms shorter.
- Useful for tree and graph problems.
- Commonly used in interview questions.

---

# Syntax

```python
def function_name():
    if base_condition:
        return

    function_name()
```

---

# Example 1

```python
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)

countdown(5)
```

Output

```
5
4
3
2
1
Done!
```

---

# Example 2

```python
def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))
```

Output

```
120
```

---

# Base Case

A **base case** is the condition that stops recursion.

Without a base case, the function will keep calling itself forever and cause an error.

Example

```python
if number == 0:
    return
```

---

# How Recursion Works

```
Function Call
      │
      ▼
Calls Itself
      │
      ▼
Base Case Reached
      │
      ▼
Function Stops
```

---

# Advantages

- Cleaner code for some problems.
- Easy to solve mathematical problems.
- Useful for trees and recursive algorithms.

---

# Disadvantages

- Can be slower than loops.
- Uses more memory.
- Infinite recursion causes `RecursionError`.

---

# Important Points

✔ Every recursive function must have a base case.

✔ A recursive call should move toward the base case.

✔ Recursion is not always the best solution.

---

# Common Mistakes

❌ Forgetting the base case.

```python
def demo():
    demo()
```

This causes a **RecursionError**.

---

# Tips

- Always write the base case first.
- Test recursion with small numbers.
- Use loops for simple repetitive tasks.

---

# Summary

In this lesson you learned:

- What is Recursion?
- Base Case
- Syntax
- Factorial Example
- Advantages and Disadvantages