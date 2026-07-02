
# Lesson 03 - Elif Statement

## What is an Elif Statement?

The `elif` statement is used to check multiple conditions.

If the first `if` condition is False, Python checks the next `elif` condition.

---

# Syntax

```python
if condition1:
    # Code
elif condition2:
    # Code
elif condition3:
    # Code
else:
    # Code
```

---

# Flow

```
Condition 1
     │
     ▼
 True?
  │
 No
  ▼
Condition 2
     │
     ▼
 True?
  │
 No
  ▼
Condition 3
     │
     ▼
Else Block
```

---

# Example 1

```python
marks = 82

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")
```

Output

```
Grade A
```

---

# Example 2

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

# Important Points

✔ `elif` means **else if**.

✔ You can use multiple `elif` blocks.

✔ Only one block is executed.

✔ `else` is optional.

---

# Common Mistakes

❌ Using `else if`

```python
else if age > 18:
```

✔ Correct

```python
elif age > 18:
```

---

❌ Wrong indentation

```python
if age > 18:
print("Adult")
```

✔ Correct

```python
if age > 18:
    print("Adult")
```

---

# Tips

- Use `elif` when checking multiple conditions.
- Arrange conditions from most specific to least specific.
- Keep conditions simple and readable.

---

# Summary

In this lesson you learned:

- What is `elif`?
- Syntax of `elif`
- Multiple conditions
- Grade calculator example
- Common mistakes