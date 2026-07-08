# Lesson 04 - Appending Files

## What is Appending?

Appending means **adding new data to the end of a file** without removing the existing content.

Python uses the **`a` (append)** mode for this purpose.

---

# Syntax

```python
file = open("notes.txt", "a")
```

---

# Writing Data

```python
file = open("notes.txt", "a")

file.write("Hello Python\n")

file.close()
```

The new text is added to the end of the file.

---

# Reading the Updated File

```python
file = open("notes.txt", "r")

print(file.read())

file.close()
```

---

# Difference Between Write and Append

| Write Mode (`w`) | Append Mode (`a`) |
|------------------|-------------------|
| Removes old data | Keeps old data |
| Writes from beginning | Adds at the end |
| Creates file if needed | Creates file if needed |

---

# Example

Existing File

```
Apple
Banana
```

Append

```python
file = open("fruits.txt", "a")
file.write("Mango\n")
```

Updated File

```
Apple
Banana
Mango
```

---

# Advantages

- Keeps previous data safe
- Adds new records easily
- Useful for logs and notes
- Commonly used in real-world applications

---

# Important Points

✔ `"a"` mode never deletes existing data.

✔ Creates a new file if it doesn't exist.

✔ Data is always added at the end.

✔ Always close the file after writing.

---

# Common Mistakes

❌ Using `"w"` instead of `"a"`.

Using `"w"` removes all previous content.

---

# Tips

- Use `\n` to write each record on a new line.
- Use append mode for logs and notes.
- Read the file after appending to verify the data.

---

# Summary

In this lesson you learned:

- Append Mode (`a`)
- Adding Data
- Reading Updated Files
- Difference Between `w` and `a`