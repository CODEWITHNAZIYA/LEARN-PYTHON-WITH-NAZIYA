# Lesson 01 - Lists

## What is a List?

A **list** is a collection of multiple items stored in a single variable.

Lists are:

- Ordered
- Mutable (changeable)
- Allow duplicate values

---

# Syntax

```python
list_name = [item1, item2, item3]
```

Example

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

# Accessing List Items

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[2])
```

Output

```
Apple
Mango
```

---

# Negative Indexing

```python
print(fruits[-1])
```

Output

```
Mango
```

---

# Adding Items

```python
fruits.append("Orange")
```

---

# Removing Items

```python
fruits.remove("Banana")
```

---

# Changing Items

```python
fruits[0] = "Grapes"
```

---

# Loop Through a List

```python
for fruit in fruits:
    print(fruit)
```

---

# Common List Methods

| Method | Description |
|---------|-------------|
| append() | Add an item |
| remove() | Remove an item |
| pop() | Remove by index |
| insert() | Insert at a position |
| sort() | Sort the list |
| reverse() | Reverse the list |
| clear() | Remove all items |
| len() | Count total items |

---

# Advantages

- Store multiple values
- Easy to modify
- Supports loops
- Built-in methods available

---

# Important Points

✔ Lists use square brackets `[]`

✔ Lists can store different data types

✔ Lists are mutable

✔ Duplicate values are allowed

---

# Common Mistakes

❌ Accessing an invalid index

```python
numbers = [1, 2, 3]

print(numbers[5])
```

This causes an **IndexError**.

---

# Tips

- Use meaningful variable names.
- Keep related data in one list.
- Use loops to process list items.

---

# Summary

In this lesson you learned:

- What is a List?
- Creating a List
- Accessing Items
- Updating Items
- Adding and Removing Items
- List Methods