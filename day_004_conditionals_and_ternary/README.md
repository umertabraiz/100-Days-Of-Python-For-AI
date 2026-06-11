# Day 4: Conditionals, Ternary Operator & Scope

Welcome to Day 4! Today we transition into control flow. You will master Python's conditional structures (`if-elif-else`), learn how to write clean inline checks using the **Ternary Operator**, and discover a critical detail about variable scope in Python blocks.

---

## 🧠 Core Concepts

### 1. Conditional Branching
Python uses indentation to define blocks of code that execute under specific conditions.
```python
x = 10
if x > 5:
    print("Greater than 5")
elif x == 5:
    print("Equal to 5")
else:
    print("Less than 5")
```

### 2. The Ternary Operator (Conditional Expression)
Instead of writing a full 4-line `if-else` statement to assign a value to a variable, Python provides a single-line expression:
```python
# Syntax: value_if_true if condition else value_if_false
status = "Access Granted" if age >= 18 else "Access Denied"
```
This is an expression, meaning it evaluates to a value that can be assigned or passed to a function.

### 3. Block Scope (Or Lack Thereof!)
This is a huge trap for developers coming from Java, C++, or JavaScript. 
In those languages, a variable declared inside an `{}` block (like an `if` statement) is local to that block and cannot be accessed outside it.

**In Python, loops and conditionals do NOT create a new scope.**
```python
if True:
    secret_key = "12345"  # Declared inside the block

print(secret_key)  # This works perfectly!
```
Variables declared inside `if` blocks or loops are available in the enclosing function or module scope. The only blocks that create new scope in Python are functions (`def`), classes (`class`), and comprehensions.

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Ternary Operator Practice
Convert the following block into a single-line ternary expression:
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```
Wait! Python's ternary operator can be chained: `A if condition_A else (B if condition_B else C)`. 
1. Implement this chained ternary operator in `practice.py` for `score = 85` and print the result.
2. Explain in comments whether you think chained ternary expressions are good for code readability.

### Exercise 2: Python's Scope Trap
Write a script that:
1. Defines a variable `threshold = 0.5`.
2. Uses an `if` statement: `if threshold > 0.8: model_version = "v2"`.
3. Outside the `if` block, print `model_version`.
4. What happens when `threshold = 0.9`? What happens when `threshold = 0.5`?
5. Write down in comments how you can prevent this potential runtime error.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. What error did you get in Exercise 2 when `threshold = 0.5`? Why did it happen?
2. How do you declare a default fallback variable in Python to avoid block-scope errors?
