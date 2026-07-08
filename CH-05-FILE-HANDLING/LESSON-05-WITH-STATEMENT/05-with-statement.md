# Lesson 05 - With Statement

## What is the With Statement?

The **with statement** is used to work with files safely.

It automatically closes the file after the block finishes.

---

# Why Use With?

Without `with`

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

With `with`

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

No need to write

```python
file.close()
```

---

# Syntax

```python
with open(file_name, mode) as file:
    # File operations
```

---

# Writing a File

```python
with open("student.txt", "w") as file:
    file.write("Naziya")
```

---

# Reading a File

```python
with open("student.txt", "r") as file:
    print(file.read())
```

---

# Appending Data

```python
with open("student.txt", "a") as file:
    file.write("\nPython")
```

---

# Advantages

- Automatically closes files
- Cleaner code
- Safer file handling
- Recommended by Python

---

# Important Points

✔ No need to call `close()`.

✔ Works with all file modes.

✔ Prevents resource leaks.

✔ Makes code easier to read.

---

# Common Mistakes

❌ Writing `file.close()` inside a `with` block.

It is unnecessary because Python closes the file automatically.

---

# Tips

- Always prefer `with` over `open()` and `close()`.
- Use it in real projects.
- Makes your code more professional.

---

# Summary

In this lesson you learned:

- What is the `with` statement?
- Syntax
- Reading files
- Writing files
- Appending files
- Advantages of `with`