# Lesson 06 - Lambda Functions

## What are Lambda Functions?

A **lambda function** is a small anonymous function.

Anonymous means the function has **no name**.

Lambda functions are useful for short and simple operations.

---

# Why Use Lambda Functions?

- Write functions in one line.
- Reduce code length.
- Improve readability for simple tasks.
- Useful with functions like `map()`, `filter()`, and `sorted()`.

---

# Syntax

```python
lambda arguments: expression
```

---

# Example 1

```python
square = lambda number: number ** 2

print(square(5))
```

Output

```
25
```

---

# Example 2

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output

```
30
```

---

# Normal Function vs Lambda Function

### Normal Function

```python
def square(number):
    return number ** 2

print(square(5))
```

### Lambda Function

```python
square = lambda number: number ** 2

print(square(5))
```

Both produce the same output.

---

# Advantages

- Short syntax
- Easy to write
- Good for small tasks
- Less code

---

# Limitations

- Only one expression is allowed.
- Not suitable for complex logic.
- Less readable for large programs.

---

# Important Points

✔ Lambda functions do not need the `def` keyword.

✔ They can take multiple arguments.

✔ They automatically return the result.

✔ Best for simple operations.

---

# Common Mistakes

❌ Trying to write multiple statements.

```python
lambda x:
    print(x)
    return x
```

This is invalid.

---

✔ Correct

```python
lambda x: x * 2
```

---

# Tips

- Use lambda functions only for simple tasks.
- Use normal functions for complex programs.
- Keep lambda expressions short and readable.

---

# Summary

In this lesson you learned:

- What is a Lambda Function?
- Syntax
- Examples
- Advantages
- Limitations