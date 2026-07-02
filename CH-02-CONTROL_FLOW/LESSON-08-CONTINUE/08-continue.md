
# Lesson 08 - Continue Statement

## What is Continue?

The `continue` statement is used to skip the current iteration of a loop.

Instead of stopping the loop completely, Python moves to the next iteration.

---

# Syntax

```python
for item in sequence:

    if condition:
        continue

    print(item)
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
continue?
  /      \
Yes      No
 │         │
Skip     Execute
Current   Code
Iteration
 │
 ▼
Next Iteration
```

---

# Example 1

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output

```
1
2
4
5
```

---

# Example 2

Print only odd numbers.

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
```

Output

```
1
3
5
7
9
```

---

# Continue vs Break

| Continue | Break |
|-----------|--------|
| Skips current iteration | Stops loop completely |
| Loop continues | Loop ends |
| Used to ignore values | Used to exit loop |

---

# Important Points

✔ `continue` skips only one iteration.

✔ The loop continues running.

✔ Works with `for` and `while` loops.

✔ Useful for filtering data.

---

# Common Mistakes

❌ Confusing `continue` with `break`

```python
if number == 5:
    continue
```

This skips only the current iteration.

---

```python
if number == 5:
    break
```

This stops the loop completely.

---

# Tips

- Use `continue` when you want to ignore specific values.
- Use `break` when you want to stop the loop.
- Keep conditions simple.

---

# Summary

In this lesson you learned:

- What is continue?
- Syntax
- For loop example
- While loop example
- Difference between break and continue