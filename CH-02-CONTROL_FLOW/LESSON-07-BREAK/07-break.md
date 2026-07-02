
# Lesson 07 - Break Statement

## What is a Break Statement?

The `break` statement is used to stop a loop immediately.

When Python executes `break`, it exits the loop without checking the remaining iterations.

---

# Syntax

```python
for item in sequence:
    if condition:
        break
```

---

# Flow

```
Start Loop
     │
     ▼
Check Condition
     │
     ▼
 break?
  /    \
Yes    No
 │      │
Exit   Continue Loop
```

---

# Example 1

```python
for i in range(1, 6):
    if i == 4:
        break

    print(i)
```

Output

```
1
2
3
```

---

# Example 2

```python
count = 1

while count <= 5:
    if count == 3:
        break

    print(count)
    count += 1
```

Output

```
1
2
```

---

# Why Do We Use Break?

- Stop a loop early.
- Exit a loop when a condition is met.
- Search operations.
- Login systems.
- Menu-driven programs.

---

# Important Points

✔ `break` works inside loops only.

✔ It immediately exits the nearest loop.

✔ It can be used in both `for` and `while` loops.

---

# Common Mistakes

❌ Using `break` outside a loop.

```python
break
```

This will produce an error.

---

✔ Correct

```python
for i in range(5):
    if i == 2:
        break
```

---

# Tips

- Use `break` only when necessary.
- Keep your loop conditions simple.
- Don't overuse `break`, as it can reduce code readability.

---

# Summary

In this lesson you learned:

- What is `break`?
- Syntax
- `for` loop example
- `while` loop example
- Common mistakes