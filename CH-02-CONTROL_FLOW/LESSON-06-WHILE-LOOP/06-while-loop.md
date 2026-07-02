
# Lesson 06 - While Loop

## What is a While Loop?

A **while loop** is used to repeat a block of code as long as a condition is **True**.

The loop stops automatically when the condition becomes **False**.

---

# Syntax

```python
while condition:
    # Code
```

---

# Flow

```
Start
  │
  ▼
Check Condition
  │
 ┌───────────┐
 │ True      │
 │           ▼
 │      Execute Code
 │           │
 └───────────┘
      │
      ▼
False → Exit Loop
```

---

# Example 1

```python
count = 1

while count <= 5:
    print(count)
    count += 1
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

# Example 2

```python
number = 5

while number > 0:
    print(number)
    number -= 1
```

Output

```
5
4
3
2
1
```

---

# Infinite Loop

An infinite loop runs forever because the condition never becomes False.

❌ Wrong

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes.

✔ Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Important Points

✔ A `while` loop depends on a condition.

✔ Update the loop variable inside the loop.

✔ Indentation is mandatory.

✔ Avoid infinite loops.

---

# Common Mistakes

❌ Forgetting to update the variable.

❌ Wrong indentation.

❌ Using a condition that never becomes False.

---

# Tips

- Use a `while` loop when you don't know the exact number of repetitions.
- Always update the loop variable.
- Test your condition carefully.

---

# Summary

In this lesson you learned:

- What is a while loop?
- Syntax
- Countdown example
- Infinite loop
- Common mistakes