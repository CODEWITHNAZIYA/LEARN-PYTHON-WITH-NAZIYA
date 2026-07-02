
# Lesson 04 - Operators

## What is an Operator?

Operators are special symbols used to perform operations on variables and values.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output

```
15
```

---

# Types of Operators in Python

## 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| // | Floor Division | 10 // 3 |
| % | Modulus | 10 % 3 |
| ** | Exponent | 2 ** 3 |

---

## 2. Comparison Operators

These operators compare two values.

Example

```python
a = 10
b = 20

print(a < b)
```

Output

```
True
```

Comparison Operators

- ==
- !=
- >
- <
- >=
- <=

---

## 3. Assignment Operators

These operators assign values.

Example

```python
num = 10

num += 5

print(num)
```

Output

```
15
```

Examples

```
=
+=
-=
*=
/=
```

---

## 4. Logical Operators

Logical operators return True or False.

Operators

- and
- or
- not

Example

```python
age = 20

print(age >= 18 and age <= 30)
```

---

## 5. Membership Operators

These operators check whether a value exists in a sequence.

Operators

```
in
not in
```

Example

```python
name = "Naziya"

print("N" in name)
```

---

## 6. Identity Operators

Identity operators compare memory locations.

Operators

```
is
is not
```

Example

```python
a = [1,2]

b = a

print(a is b)
```

---

# Common Mistakes

❌ Using = instead of ==

Wrong

```python
if a = 10:
```

Correct

```python
if a == 10:
```

---

# Tips

✔ Learn arithmetic operators first.

✔ Practice comparison operators daily.

✔ Remember:

- == compares values

- is compares objects

---

# Summary

In this lesson you learned

- Arithmetic Operators
- Comparison Operators
- Assignment Operators
- Logical Operators
- Membership Operators
- Identity Operators