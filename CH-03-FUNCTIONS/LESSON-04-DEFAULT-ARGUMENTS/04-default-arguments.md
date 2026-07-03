# Lesson 04 - Default Arguments

## What are Default Arguments?

A **default argument** is a parameter that already has a default value.

If no value is passed while calling the function, Python uses the default value automatically.

---

# Why Use Default Arguments?

- Reduce repeated code.
- Make functions easier to use.
- Avoid passing the same value every time.
- Improve code readability.

---

# Syntax

```python
def function_name(parameter="default_value"):
    # Code
```

---

# Example 1

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Naziya")
```

Output

```
Hello Guest
Hello Naziya
```

---

# Example 2

```python
def power(number, exponent=2):
    return number ** exponent

print(power(5))
print(power(5, 3))
```

Output

```
25
125
```

---

# Rules of Default Arguments

✔ Parameters with default values should come after required parameters.

✔ Correct

```python
def student(name, course="Python"):
    pass
```

❌ Wrong

```python
def student(course="Python", name):
    pass
```

---

# Important Points

✔ Default values are optional.

✔ You can override the default value.

✔ Functions become more flexible.

---

# Common Mistakes

❌ Forgetting the correct parameter order.

❌ Assuming the default value cannot be changed.

---

# Tips

- Use default arguments for commonly used values.
- Keep default values simple.
- Use meaningful parameter names.

---

# Summary

In this lesson you learned:

- What are default arguments?
- Syntax
- Rules
- Examples
- Common mistakes