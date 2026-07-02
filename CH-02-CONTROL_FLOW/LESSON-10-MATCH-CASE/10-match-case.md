
# Lesson 10 - Match Case

## What is Match Case?

`match-case` is a decision-making statement introduced in **Python 3.10**.

It is used as an alternative to long `if-elif-else` statements.

---

# Syntax

```python
match variable:
    case value1:
        # Code
    case value2:
        # Code
    case _:
        # Default Code
```

---

# Example 1

```python
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid Day")
```

Output

```
Tuesday
```

---

# Example 2

```python
fruit = "Apple"

match fruit:
    case "Apple":
        print("Red Fruit")
    case _:
        print("Unknown Fruit")
```

---

# Default Case

The underscore (`_`) works like the `else` block.

```python
case _:
    print("Invalid Input")
```

---

# Why Use Match Case?

- Cleaner than multiple `if-elif`.
- Easy to read.
- Better for menu-driven programs.
- Useful when checking many fixed values.

---

# Important Points

✔ Available in Python 3.10 or above.

✔ `case _` acts as the default case.

✔ Only one matching case executes.

---

# Common Mistakes

❌ Using `match-case` in Python versions below 3.10.

❌ Forgetting the default (`case _`) block.

---

# Tips

- Use `match-case` when comparing one variable with many fixed values.
- Use `if-elif` when conditions involve ranges or complex comparisons.

---

# Summary

In this lesson you learned:

- What is Match Case?
- Syntax
- Default case
- Calculator example
- Day example