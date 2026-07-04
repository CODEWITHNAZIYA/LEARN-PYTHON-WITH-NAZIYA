# Lesson 03 - Sets

## What is a Set?

A **set** is a collection of unique items.

Sets are:

- Unordered
- Mutable (changeable)
- Do not allow duplicate values

---

# Syntax

```python
set_name = {item1, item2, item3}
```

Example

```python
fruits = {"Apple", "Banana", "Mango"}
```

---

# Adding Items

```python
fruits.add("Orange")
```

---

# Removing Items

```python
fruits.remove("Banana")
```

---

# Loop Through a Set

```python
for fruit in fruits:
    print(fruit)
```

---

# Set Operations

## Union

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
```

Output

```
{1, 2, 3, 4, 5}
```

---

## Intersection

```python
print(A.intersection(B))
```

Output

```
{3}
```

---

## Difference

```python
print(A.difference(B))
```

Output

```
{1, 2}
```

---

# Common Set Methods

| Method | Description |
|---------|-------------|
| add() | Add an item |
| remove() | Remove an item |
| pop() | Remove a random item |
| clear() | Remove all items |
| union() | Combine sets |
| intersection() | Common items |
| difference() | Different items |
| len() | Count total items |

---

# Advantages

- Automatically removes duplicates
- Fast searching
- Supports mathematical operations
- Easy to use

---

# Important Points

✔ Uses curly braces `{}`

✔ Duplicate values are not allowed

✔ Items are unordered

✔ Sets are mutable

---

# Common Mistakes

❌ Expecting items to appear in the same order.

```python
numbers = {1, 2, 3}

print(numbers)
```

The output order may change.

---

# Tips

- Use sets to remove duplicate values.
- Use set operations for comparisons.
- Don't rely on item order.

---

# Summary

In this lesson you learned:

- What is a Set?
- Creating Sets
- Adding and Removing Items
- Set Operations
- Set Methods