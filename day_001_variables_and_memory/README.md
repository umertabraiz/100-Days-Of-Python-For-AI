# Day 1: Python Memory Model, Variables & Identity

Welcome to Day 1! Today, we are going deep under the hood of Python. You might already know how to write `x = 5`, but do you know what Python actually does in memory?

## 🧠 Core Concept: Everything is an Object & Variables are Labels

In Python:
1. **Variables are names (labels) bound to objects.** They are not boxes that hold values; they are pointers or references to objects in memory.
2. **Objects have three properties:**
   - **Identity (`id()`):** The unique address of the object in memory.
   - **Type (`type()`):** The class of the object (e.g., `int`, `str`, `list`).
   - **Value:** The data represented by the object.

### 🔍 Socratic Experiment: Reference vs. Value
What do you think happens when we run the following code?
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```
- Does `a` change? Why or why not?
- If we do `x = 5` and `y = 5`, do they point to the same address? What about `x = 1000` and `y = 1000`? (Look up "Integer Caching / Interning" in Python).

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Object Identity Challenge
Write a script that:
1. Creates two variables, `list1` and `list2`, both initialized with the value `[10, 20, 30]`.
2. Compares them using `==` (equality) and `is` (identity). Print the results.
3. Explains in comments what the difference between `==` and `is` is.
4. Modifies `list1` by appending `40`. Check if `list2` changes.
5. Now create `list3 = list1`. Compare them using `==` and `is`. Modifies `list3` and check if `list1` changes.

### Exercise 2: The Integer Caching Mystery
Write a script that:
1. Compares `x = 256` and `y = 256` using `is`.
2. Compares `x = 257` and `y = 257` using `is`.
3. Run this script in two ways:
   - Run it directly in the terminal as `python practice.py`.
   - Run it line-by-line in an interactive Python shell (REPL).
4. Do you see a difference? Can you explain why Python caches small integers but behaves differently with larger ones or when compiled as a single block of code?

---

## 💬 Socratic Discussion
Once you have created and run `practice.py`, respond to me with:
1. Your code and the output you observed.
2. Your answers to the Socratic questions:
   - What is the difference between `==` and `is`?
   - Why did `list2` NOT change when you appended to `list1`, but `list1` DID change when you modified `list3`?
   - What did you discover about integer caching (interning)?
