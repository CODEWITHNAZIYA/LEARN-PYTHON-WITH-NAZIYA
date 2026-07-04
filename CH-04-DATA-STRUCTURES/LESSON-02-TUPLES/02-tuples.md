# Lesson 02 - Tuples

## What is a Tuple?

A **tuple** is a collection of multiple items stored in a single variable.

Tuples are:

- Ordered
- Immutable (cannot be changed)
- Allow duplicate values

---

# Syntax

```python
tuple_name = (item1, item2, item3)
```

Example

```python
fruits = ("Apple", "Banana", "Mango")
```

---

# Accessing Tuple Items

```python
fruits = ("Apple", "Banana", "Mango")

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

# Loop Through a Tuple

```python
for fruit in fruits:
    print(fruit)
```

---

# Tuple Methods

| Method | Description |
|---------|-------------|
| count() | Counts occurrences of an item |
| index() | Returns the index of an item |
| len() | Returns total items |

---

# Advantages

- Faster than lists
- Uses less memory
- Data remains safe
- Good for fixed values

---

# Important Points

✔ Tuples use parentheses `()`

✔ Tuples are immutable

✔ Duplicate values are allowed

✔ Different data types can be stored

---

# Difference Between List and Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Slower | Faster |

---

# Common Mistakes

❌ Trying to change a tuple item.

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This causes a **TypeError**.

---

# Tips

- Use tuples for fixed data.
- Use lists when data needs to change.
- Tuples are ideal for storing constants.

---

# Summary

In this lesson you learned:

- What is a Tuple?
- Creating Tuples
- Accessing Items
- Tuple Methods
- List vs Tuple