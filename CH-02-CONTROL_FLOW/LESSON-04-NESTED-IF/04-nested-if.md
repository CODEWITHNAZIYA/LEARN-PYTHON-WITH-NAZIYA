
# Lesson 04 - Nested If

## What is a Nested If?

A **Nested If** means placing one `if` statement inside another `if` statement.

It is useful when one condition depends on another condition.

---

# Syntax

```python
if condition1:
    if condition2:
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
    Yes
     │
Condition 2
     │
     ▼
 True?
  /      \
Yes      No
 |        |
Code   Skip Code
```

---

# Example 1

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Eligible")
```

Output

```
Eligible
```

---

# Example 2

```python
marks = 80
attendance = 85

if marks >= 35:
    if attendance >= 75:
        print("Pass")
```

Output

```
Pass
```

---

# When to Use Nested If?

Use Nested If when:

- One condition depends on another.
- Multiple checks are required.
- Login systems.
- Student result systems.
- Permission checking.

---

# Important Points

✔ An `if` statement can contain another `if`.

✔ Proper indentation is required.

✔ The inner `if` runs only if the outer `if` is True.

---

# Common Mistakes

❌ Wrong Indentation

```python
if age >= 18:
if has_id:
print("Allowed")
```

✔ Correct

```python
if age >= 18:
    if has_id:
        print("Allowed")
```

---

# Tips

- Avoid too many nested levels.
- Keep conditions simple.
- Use meaningful variable names.

---

# Summary

In this lesson you learned:

- What is Nested If?
- Syntax
- Login example
- Student result example
- Common mistakes