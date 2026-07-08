# Lesson 06 - File Modes

## What are File Modes?

File modes tell Python **how to open a file**.

Different modes are used for reading, writing, appending, and creating files.

---

# Common File Modes

| Mode | Description |
|------|-------------|
| `r` | Read a file |
| `w` | Write to a file (overwrites existing data) |
| `a` | Append data to the end of a file |
| `x` | Create a new file (raises an error if it already exists) |

---

# Read Mode (`r`)

Reads an existing file.

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

---

# Write Mode (`w`)

Writes data into a file.

```python
with open("student.txt", "w") as file:
    file.write("Hello")
```

If the file exists, old data is removed.

---

# Append Mode (`a`)

Adds new data to the end of a file.

```python
with open("student.txt", "a") as file:
    file.write("\nPython")
```

---

# Create Mode (`x`)

Creates a new file.

```python
with open("new.txt", "x") as file:
    file.write("Hello")
```

If the file already exists, Python raises:

```
FileExistsError
```

---

# Comparison Table

| Mode | Creates File | Deletes Old Data | Adds New Data |
|------|--------------|------------------|---------------|
| `r` | ❌ No | ❌ No | ❌ No |
| `w` | ✅ Yes | ✅ Yes | ✅ Yes |
| `a` | ✅ Yes | ❌ No | ✅ At End |
| `x` | ✅ Yes | ❌ No | ✅ New File |

---

# Advantages

- Easy file management
- Permanent data storage
- Useful in real-world applications
- Supports different operations

---

# Important Points

✔ Use `r` to read files.

✔ Use `w` to overwrite files.

✔ Use `a` to keep old data.

✔ Use `x` to safely create a new file.

---

# Tips

- Use `with` for better file handling.
- Always choose the correct mode.
- Handle errors using `try-except`.

---

# Summary

In this lesson you learned:

- File Modes
- Read Mode
- Write Mode
- Append Mode
- Create Mode