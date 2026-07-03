# Lesson 03 - Return Statement

## What is Return?

The `return` statement is used to send a value back from a function.

After `return` executes, the function ends immediately.

---

# Why Use Return?

- Return results from a function.
- Reuse calculated values.
- Write cleaner code.
- Build larger programs using functions.

---

# Syntax

```python
def function_name():
    return value
```

---

# Example 1

```python
def greet():
    return "Hello"

message = greet()
print(message)
```

Output

```
Hello
```

---

# Example 2

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output

```
30
```

---

# Return vs Print

### Using print()

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output

```
30
```

The value is displayed but cannot be reused.

---

### Using return

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output

```
30
```

The value can be stored and reused.

---

# How Return Works

```
Function Called
      │
      ▼
Execute Code
      │
      ▼
Return Value
      │
      ▼
Store or Use Result
```

---

# Important Points

✔ `return` ends the function.

✔ A function can return any data type.

✔ Returned values can be stored in variables.

✔ `return` is different from `print()`.

---

# Common Mistakes

❌ Forgetting to store the returned value.

```python
def add(a, b):
    return a + b

add(10, 20)
```

---

✔ Correct

```python
result = add(10, 20)
print(result)
```

---

# Tips

- Use `return` when you need the result later.
- Use meaningful variable names.
- Avoid unnecessary `print()` inside reusable functions.

---

# Summary

In this lesson you learned:

- What is `return`?
- Return syntax
- Return vs Print
- Reusing returned values
- Common mistakes