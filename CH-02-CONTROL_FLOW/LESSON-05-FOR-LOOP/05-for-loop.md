
# Lesson 05 - For Loop

## What is a For Loop?

A **for loop** is used to repeat a block of code multiple times.

It is commonly used when the number of repetitions is known.

---

# Syntax

```python
for variable in sequence:
    # Code
```

---

# Using range()

The `range()` function generates a sequence of numbers.

Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output

```
1
2
3
4
5
```

---

# range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

Output

```
2
4
6
8
10
```

---

# Loop Through a String

```python
name = "Python"

for letter in name:
    print(letter)
```

---

# Loop Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

# Important Points

✔ A `for` loop repeats code.

✔ `range()` is commonly used with `for`.

✔ Indentation is required.

✔ The loop ends automatically.

---

# Common Mistakes

❌ Missing colon

```python
for i in range(5)
```

✔ Correct

```python
for i in range(5):
```

---

❌ Wrong indentation

```python
for i in range(5):
print(i)
```

✔ Correct

```python
for i in range(5):
    print(i)
```

---

# Tips

- Use meaningful variable names.
- Practice with `range()`.
- Use loops to avoid writing repetitive code.

---

# Summary

In this lesson you learned:

- What is a for loop?
- range()
- Looping through strings
- Looping through lists
- Common mistakes