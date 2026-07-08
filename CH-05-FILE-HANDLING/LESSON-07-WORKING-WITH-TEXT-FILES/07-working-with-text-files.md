# Lesson 07 - Working With Text Files

## What are Text Files?

A text file is a file that stores information in plain text.

Examples:

- notes.txt
- student.txt
- diary.txt
- report.txt

---

# Why Use Text Files?

- Store notes
- Save user data
- Create reports
- Maintain logs
- Save application data

---

# Creating a Text File

```python
with open("notes.txt", "w") as file:
    file.write("Hello Python")
```

---

# Reading a Text File

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

---

# Appending Data

```python
with open("notes.txt", "a") as file:
    file.write("\nKeep Learning")
```

---

# Reading Line by Line

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line)
```

---

# Counting Lines

```python
with open("notes.txt", "r") as file:
    lines = file.readlines()

print(len(lines))
```

---

# Counting Words

```python
with open("notes.txt", "r") as file:
    words = file.read().split()

print(len(words))
```

---

# Real-Life Uses

- Student records
- Attendance system
- Notes application
- Employee details
- Daily logs

---

# Advantages

- Easy to use
- Human-readable
- Permanent data storage
- Useful for beginners

---

# Important Points

✔ Use `with` whenever possible.

✔ Close files automatically.

✔ Use `split()` to count words.

✔ Use `readlines()` to count lines.

---

# Tips

- Keep file names meaningful.
- Store one record per line.
- Always handle file errors.

---

# Summary

In this lesson you learned:

- Working with text files
- Reading and writing
- Appending data
- Counting lines
- Counting words
- Real-world examples