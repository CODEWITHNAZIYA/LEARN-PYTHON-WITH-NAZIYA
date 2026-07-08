# Lesson 01 - File Basics

## What is File Handling?

**File Handling** is the process of creating, reading, writing, and managing files using Python.

It allows data to be stored permanently instead of only during program execution.

---

# Why Do We Need Files?

- Store data permanently
- Read saved information
- Save user input
- Create reports
- Manage project data

---

# open() Function

Python uses the `open()` function to work with files.

Syntax

```python
open(file_name, mode)
```

Example

```python
file = open("sample.txt", "w")
```

---

# Closing a File

Always close a file after using it.

```python
file.close()
```

---

# Example

```python
file = open("sample.txt", "w")
file.write("Hello World")
file.close()
```

---

# Reading a File

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

---

# File Modes

| Mode | Description |
|------|-------------|
| r | Read a file |
| w | Write a file |
| a | Append data |
| x | Create a new file |

---

# Advantages

- Permanent data storage
- Easy to manage information
- Useful in real-world applications

---

# Important Points

✔ Always close the file after use.

✔ Use the correct file mode.

✔ A file can contain text or other data.

---

# Common Mistakes

❌ Trying to read a file that doesn't exist.

```python
open("demo.txt", "r")
```

This causes a **FileNotFoundError**.

---

# Tips

- Use meaningful file names.
- Close every file after use.
- Keep files in the project folder.

---

# Summary

In this lesson you learned:

- What is File Handling?
- open()
- close()
- Creating a File
- Reading a File
- File Modes