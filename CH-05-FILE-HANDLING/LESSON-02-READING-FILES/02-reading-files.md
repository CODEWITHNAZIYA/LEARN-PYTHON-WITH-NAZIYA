# Lesson 02 - Reading Files

## What is Reading a File?

Reading a file means retrieving the data stored inside a file.

Python provides different methods to read file contents.

---

# Opening a File

```python
file = open("sample.txt", "r")
```

`r` stands for **Read Mode**.

---

# read()

Reads the complete file.

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

# readline()

Reads only one line.

```python
file = open("sample.txt", "r")

print(file.readline())

file.close()
```

---

# readlines()

Reads all lines and returns a list.

```python
file = open("sample.txt", "r")

print(file.readlines())

file.close()
```

---

# Reading Using Loop

```python
file = open("sample.txt", "r")

for line in file:
    print(line)

file.close()
```

---

# FileNotFoundError

If the file doesn't exist,

```python
open("demo.txt", "r")
```

Python raises

```
FileNotFoundError
```

---

# Common Reading Methods

| Method | Description |
|---------|-------------|
| read() | Reads complete file |
| readline() | Reads one line |
| readlines() | Reads all lines as a list |

---

# Advantages

- Read stored information
- Process text files
- Display saved data
- Useful for reports

---

# Important Points

✔ Always open in `r` mode.

✔ Close the file after reading.

✔ Handle missing files using `try-except`.

---

# Tips

- Use `read()` for small files.
- Use loops for large files.
- Always handle file errors.

---

# Summary

In this lesson you learned:

- read()
- readline()
- readlines()
- Reading using loops
- FileNotFoundError