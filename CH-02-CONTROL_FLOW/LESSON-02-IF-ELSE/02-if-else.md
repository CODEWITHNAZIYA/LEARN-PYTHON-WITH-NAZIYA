
# Lesson 02 - If Else Statement

## What is an If Else Statement?

The `if-else` statement is used to make decisions between two choices.

- If the condition is **True**, the `if` block runs.
- If the condition is **False**, the `else` block runs.

---

# Syntax

```python
if condition:
    # Code if condition is True
else:
    # Code if condition is False
```

---

# Flow

```
Condition
     │
     ▼
  True ?
  /    \
Yes    No
 |      |
If    Else
Block  Block
```

---

# Example 1

```python
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Output

```
Eligible
```

---

# Example 2

```python
marks = 30

if marks >= 35:
    print("Pass")
else:
    print("Fail")
```

Output

```
Fail
```

---

# Example 3

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# Important Points

✔ `if` checks the condition.

✔ `else` runs only when the condition is False.

✔ Only one block is executed.

✔ Indentation is mandatory.

---

# Common Mistakes

❌ Missing colon

```python
if age >= 18
```

✔ Correct

```python
if age >= 18:
```

---

❌ Wrong indentation

```python
if age >= 18:
print("Eligible")
else:
print("Not Eligible")
```

✔ Correct

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# Tips

- Use `if-else` when there are only two possible outcomes.
- Keep conditions simple.
- Test both True and False cases.

---

# Summary

In this lesson you learned:

- What is if-else?
- Syntax
- Decision making
- Even/Odd example
- Voting example
- Common mistakes