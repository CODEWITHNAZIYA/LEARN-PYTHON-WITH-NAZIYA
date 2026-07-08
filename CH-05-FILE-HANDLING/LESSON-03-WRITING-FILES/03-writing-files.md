# Lesson 03 - Writing Files

## What is Writing to a File?

Writing means storing data inside a file.

Python uses the **write()** method to save text into a file.

---

# Write Mode

```python
file = open("student.txt", "w")
```

The `"w"` mode:

- Creates a new file if it doesn't exist.
- Overwrites the existing file.

---

# Writing Data

```python
file = open("student.txt", "w")

file.write("Hello World")

file.close()
```

---

# Writing Multiple Lines

```python
file = open("student.txt", "w")

file.write("Name: Ali\n")
file.write("Age: 20\n")
file.write("Course: Python")

file.close()
```

---

# Reading the Written Data

```python
file = open("student.txt", "r")

print(file.read())

file.close()
```

---

# Important Note

Using `"w"` mode removes all previous content before writing new data.

Example

Old File

```
Hello
```

After

```python
open("file.txt","w")
```

New File

```
(empty)
```

---

# Advantages

- Save user information
- Create reports
- Store program output
- Generate text files

---

# Important Points

✔ `write()` writes text into a file.

✔ `"w"` creates a file if it doesn't exist.

✔ `"w"` deletes previous content.

✔ Always close the file after writing.

---

# Common Mistakes

❌ Forgetting to close the file.

❌ Expecting `"w"` mode to keep old data.

---

# Tips

- Use `\n` for new lines.
- Read the file after writing to verify the content.
- Use meaningful file names.

---

# Summary

In this lesson you learned:

- write()
- Write Mode
- Creating Files
- Writing Multiple Lines
- Reading Written Data