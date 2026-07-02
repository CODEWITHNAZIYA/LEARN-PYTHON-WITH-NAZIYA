
# Lesson 07 - Keywords

## What are Keywords?

Keywords are reserved words in Python.

They have a special meaning and cannot be used as variable names.

Example

```python
if
else
for
while
True
False
None
```

---

# Why are Keywords Important?

Keywords help Python understand the program.

Each keyword has its own purpose.

For example,

- `if` is used for decision making.
- `for` is used for loops.
- `def` is used to create functions.

---

# How to View All Keywords?

Python provides a built-in module called `keyword`.

Example

```python
import keyword

print(keyword.kwlist)
```

---

# Common Python Keywords

| Keyword | Purpose |
|----------|----------|
| if | Decision Making |
| else | Alternative Condition |
| elif | Multiple Conditions |
| for | Loop |
| while | Loop |
| break | Exit Loop |
| continue | Skip Current Iteration |
| pass | Empty Block |
| True | Boolean Value |
| False | Boolean Value |
| None | Represents No Value |
| and | Logical Operator |
| or | Logical Operator |
| not | Logical Operator |
| def | Create Function |
| return | Return Value |
| import | Import Module |
| class | Create Class |
| try | Exception Handling |
| except | Handle Errors |

---

# Example

```python
age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Output

```
Eligible
```

---

# Rules

✔ Keywords are case-sensitive.

✔ Keywords cannot be used as variable names.

✔ Every keyword has a fixed meaning.

---

# Common Mistakes

❌ Wrong

```python
if = 10
```

❌ Wrong

```python
for = "Python"
```

✔ Correct

```python
age = 10

name = "Naziya"
```

---

# Tips

- Learn keywords one by one.
- Practice them with examples.
- Never use keywords as variable names.

---

# Summary

In this lesson you learned:

- What are keywords?
- Why keywords are important
- Python keyword module
- Common Python keywords
- Rules for using keywords