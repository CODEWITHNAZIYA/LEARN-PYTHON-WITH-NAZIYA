
# Lesson 05 - Strings

## What is a String?

A string is a sequence of characters.

Strings are used to store text data like names, addresses, messages, etc.

Example

```python
name = "Naziya"
```

---

# Creating Strings

You can create strings using:

- Single Quotes

```python
name = 'Python'
```

- Double Quotes

```python
name = "Python"
```

- Triple Quotes

```python
text = """Hello Everyone"""
```

---

# String Indexing

Each character has an index.

Example

```python
word = "Python"

print(word[0])
print(word[1])
```

Output

```
P
y
```

---

# String Slicing

Slicing is used to get a part of a string.

Example

```python
word = "Python"

print(word[0:3])
```

Output

```
Pyt
```

---

# Useful String Methods

## upper()

Converts text into uppercase.

```python
name = "python"

print(name.upper())
```

---

## lower()

Converts text into lowercase.

---

## title()

Makes the first letter of each word capital.

---

## capitalize()

Makes only the first letter capital.

---

## replace()

Replaces one word with another.

Example

```python
text = "I love Java"

print(text.replace("Java", "Python"))
```

---

## find()

Finds the position of a word.

---

## count()

Counts how many times a character appears.

---

# String Concatenation

Concatenation means joining two strings.

Example

```python
first = "Hello"

second = "World"

print(first + " " + second)
```

---

# String Formatting

Using f-string

```python
name = "Naziya"

print(f"Welcome {name}")
```

---

# Escape Characters

Example

```python
print("Hello\nWorld")
```

Common Escape Characters

| Character | Meaning |
|-----------|---------|
| \n | New Line |
| \t | Tab |
| \" | Double Quote |

---

# Common Mistakes

❌ Forgetting quotation marks

Wrong

```python
name = Python
```

Correct

```python
name = "Python"
```

---

# Tips

✔ Strings are immutable.

✔ Index starts from 0.

✔ Negative indexing starts from -1.

✔ Use f-strings for better formatting.

---

# Summary

In this lesson you learned

- Creating Strings
- Indexing
- Slicing
- String Methods
- Concatenation
- Formatting
- Escape Characters