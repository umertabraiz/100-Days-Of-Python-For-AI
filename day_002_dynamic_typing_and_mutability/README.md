# Day 2: Dynamic Typing, Mutability & Reference Counting

Welcome to Day 2! Yesterday we learned that variables are labels pointing to objects in memory. Today, we look at how the objects themselves behave: their types, whether they can be changed, and how Python cleans them up when we are done.

---

## 🧠 Core Concepts

### 1. Dynamic Typing: Names Have No Type
In statically typed languages (like C++ or Java), you declare `int x = 5;`. The type is bound to the variable name.
In Python, you write `x = 5`. The variable `x` is just a label. The type `int` is bound to the **object `5`** itself.
If you later write `x = "hello"`, Python simply rebinds the label `x` to a new `str` object `"hello"`.

### 2. Mutability vs. Immutability
Objects in Python are either:
- **Mutable (changeable in-place):** `list`, `dict`, `set`, and user-defined classes. Their value can change without changing their identity (`id()`).
- **Immutable (unchangeable):** `int`, `float`, `str`, `tuple`, `bool`, `frozenset`. If you try to modify them, Python creates a new object in memory and updates the variable to point to it.

#### 🔍 Socratic Experiment: String Modification
What do you think happens in memory when we run this?
```python
s = "Python"
print(id(s))
s += " 3"
print(id(s))
```
Does the ID stay the same? Why or why not?

### 3. Reference Counting & Garbage Collection
How does Python free up memory?
Python uses **Reference Counting** as its primary garbage collection mechanism. Every object keeps track of how many variables or collections point to it.
- When you do `a = [1, 2]`, the list object's reference count is `1`.
- When you do `b = a`, the reference count becomes `2`.
- When you do `a = None` and `b = None`, the reference count drops to `0`.
- Once the count reaches `0`, Python automatically deallocates the object from memory.

You can inspect an object's reference count using `sys.getrefcount(obj)`. Note that passing the object to `getrefcount()` temporarily increases the count by `1` because the function parameter also references it.

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Mutability & Memory Addresses
Write a script to prove that lists are mutable and strings are immutable:
1. Create a list `my_list = [1, 2, 3]`. Print its initial `id()`.
2. Append `4` to `my_list`. Print its new `id()`. Did it change?
3. Create a string `my_str = "Hello"`. Print its initial `id()`.
4. Concatenate `" World"` to `my_str`. Print its new `id()`. Did it change?
5. Write down in comments why this difference matters when writing efficient code (e.g., building strings in loops).

### Exercise 2: The Tuple Mutability Loophole
Tuples are immutable, but what if they contain mutable objects?
1. Create a tuple `my_tuple = (1, 2, [3, 4])`.
2. Try to change the first element: `my_tuple[0] = 100`. (Observe the error).
3. Try to modify the list inside the tuple: `my_tuple[2].append(5)`. Did it succeed?
4. Print the tuple. Explain in comments how an immutable container can hold elements that change.

### Exercise 3: Reference Counting Investigation
Use `sys.getrefcount` to observe references:
1. Import `sys`.
2. Create a large unique list `a = [999] * 1000`.
3. Check the reference count of `a`. (Explain why the count is 2 and not 1).
4. Create references `b = a` and `c = a`. Check the reference count of `a` again.
5. Delete `b` using `del b`. Check the reference count of `a` again.

---

## 💬 Socratic Discussion
Once you run `practice.py`, tell me:
1. What were the results of the 3 exercises?
2. Why does modifying a list keep the same `id()`, but modifying a string changes it?
3. Why was the list inside the tuple modifiable even though the tuple itself is immutable?
