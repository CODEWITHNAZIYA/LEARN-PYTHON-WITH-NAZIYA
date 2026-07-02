
# Lesson 09 - Pass Statement

## What is the Pass Statement?

The `pass` statement is a **placeholder** in Python.

It does nothing when executed.

It is mainly used when a block of code is required syntactically, but you don't want to write the implementation yet.

---

# Syntax

```python
if condition:
    pass
```

---

# Example 1

```python
age = 20

if age >= 18:
    pass

print("Done")
```

Output

```
Done
```

---

# Example 2

```python
for i in range(5):
    if i == 2:
        pass

    print(i)
```

Output

```
0
1
2
3
4
```

---

# Example 3

```python
def greet():
    pass
```

The function is created successfully but does nothing.

---

# Why Do We Use Pass?

- Placeholder for future code.
- Create empty functions.
- Create empty classes.
- Create empty loops.
- Avoid syntax errors.

---

# Important Points

✔ `pass` does nothing.

✔ It prevents syntax errors.

✔ It is useful during development.

✔ The program continues normally.

---

# Common Mistakes

❌ Empty block

```python
if age >= 18:
```

This gives an **IndentationError**.

---

✔ Correct

```python
if age >= 18:
    pass
```

---

# Tips

- Use `pass` only as a temporary placeholder.
- Replace it with actual code later.
- Don't leave unnecessary `pass` statements in finished projects.

---

# Summary

In this lesson you learned:

- What is `pass`?
- Syntax
- Empty functions
- Empty loops
- Placeholder concept