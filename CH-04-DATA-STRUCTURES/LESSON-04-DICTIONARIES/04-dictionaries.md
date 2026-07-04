# Lesson 04 - Dictionaries

## What is a Dictionary?

A **dictionary** is a collection of data stored in **key-value pairs**.

Dictionaries are:

- Ordered
- Mutable (changeable)
- Do not allow duplicate keys

---

# Syntax

```python
dictionary_name = {
    "key1": value1,
    "key2": value2
}
```

Example

```python
student = {
    "name": "Naziya",
    "age": 21
}
```

---

# Accessing Values

```python
print(student["name"])
```

Output

```
Naziya
```

---

# Adding a New Item

```python
student["city"] = "Surat"
```

---

# Updating a Value

```python
student["age"] = 22
```

---

# Removing an Item

```python
student.pop("age")
```

---

# Loop Through Dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

# Common Dictionary Methods

| Method | Description |
|---------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Gets the value of a key |
| update() | Updates the dictionary |
| pop() | Removes a key |
| clear() | Removes all items |
| len() | Returns total items |

---

# Advantages

- Fast data lookup
- Easy to update
- Stores related data together
- Uses meaningful keys

---

# Important Points

✔ Uses curly braces `{}`

✔ Stores data as key-value pairs

✔ Keys must be unique

✔ Values can be duplicated

✔ Dictionaries are mutable

---

# Common Mistakes

❌ Accessing a key that doesn't exist.

```python
student = {
    "name": "Ali"
}

print(student["age"])
```

This causes a **KeyError**.

Use `get()` to avoid errors.

```python
print(student.get("age"))
```

---

# Tips

- Use meaningful key names.
- Use `get()` when you're not sure a key exists.
- Dictionaries are ideal for storing related information.

---

# Summary

In this lesson you learned:

- What is a Dictionary?
- Creating Dictionaries
- Adding and Updating Data
- Removing Items
- Dictionary Methods