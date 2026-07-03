# Lesson 05 - Keyword Arguments

## What are Keyword Arguments?

Keyword arguments allow us to pass values to a function using the **parameter names**.

The order of arguments does not matter when using keyword arguments.

---

# Why Use Keyword Arguments?

- Makes code more readable.
- Arguments can be passed in any order.
- Reduces confusion.
- Improves code clarity.

---

# Syntax

```python
function_name(parameter=value)
```

---

# Example 1

```python
def student(name, age):
    print(name)
    print(age)

student(name="Naziya", age=21)
```

Output

```
Naziya
21
```

---

# Example 2

```python
def employee(name, department):
    print(name)
    print(department)

employee(department="IT", name="Ali")
```

Output

```
Ali
IT
```

Notice that the order is different, but the output is correct because parameter names are used.

---

# Positional vs Keyword Arguments

## Positional Arguments

```python
student("Naziya", 21)
```

Arguments must be in the correct order.

---

## Keyword Arguments

```python
student(age=21, name="Naziya")
```

Arguments can be passed in any order.

---

# Advantages

- Easy to understand
- More readable
- Flexible
- Reduces mistakes

---

# Important Points

✔ Use parameter names while passing values.

✔ Order does not matter.

✔ You can combine positional and keyword arguments.

Example:

```python
student("Naziya", age=21)
```

---

# Common Mistakes

❌ Using the same parameter twice.

```python
student("Naziya", name="Ali")
```

This will produce an error.

---

# Tips

- Use keyword arguments when a function has many parameters.
- Write meaningful parameter names.
- Keep your code readable.

---

# Summary

In this lesson you learned:

- Keyword Arguments
- Syntax
- Advantages
- Positional vs Keyword Arguments
- Common mistakes