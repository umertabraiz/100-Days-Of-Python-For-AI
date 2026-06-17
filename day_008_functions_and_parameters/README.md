# Day 8: Functions, Arguments & The Mutable Default Trap

Welcome to Day 8! Today we begin our deep dive into **Functions**. Functions are the primary building blocks of Python software, and in AI (like PyTorch or Hugging Face), you will constantly interact with functions that have dozens of optional parameters.

Today, you will learn the difference between positional and keyword arguments, and master a famous Python trap: **using mutable default arguments**.

---

## 🧠 Core Concepts

### 1. Positional vs. Keyword Arguments
* **Positional Arguments**: Mapped to parameters in the order they are passed.
* **Keyword Arguments**: Passed with the parameter name explicitly defined. You can pass them in any order!

```python
def describe_model(name, layers, framework):
    print(f"Model: {name} | Layers: {layers} | Framework: {framework}")

# Positional (Order matters!)
describe_model("ResNet", 50, "PyTorch")

# Keyword (Order doesn't matter!)
describe_model(framework="TensorFlow", name="BERT", layers=12)
```

### 2. Default Values (Optional Parameters)
You can assign default values to parameters to make them optional:
```python
def greet(name="AI Engineer"):
    print(f"Hello, {name}!")

greet()         # Outputs: Hello, AI Engineer!
greet("Umer")   # Outputs: Hello, Umer!
```
*Note: Parameters with default values must always come after parameters without default values.*

### 3. The Mutable Default Trap (Critical Interview Question!)
What happens if you use a mutable object (like a list `[]` or a dictionary `{}`) as a default value?

```python
def add_to_batch(item, batch=[]):
    batch.append(item)
    return batch

# Let's run it:
print(add_to_batch("image1"))  # Output: ['image1']
print(add_to_batch("image2"))  # Output: ['image1', 'image2']  <-- Wait, what?!
```
**Why did this happen?**
In Python, default arguments are evaluated **only once, when the function is defined**, not every time the function is called. This means that the exact same list object in memory is shared across all function calls!

#### 🛡️ The Correct Pattern:
Use `None` as the default value, and create a new list inside the function:
```python
def add_to_batch(item, batch=None):
    if batch is None:
        batch = []  # Creates a fresh list in memory for each call
    batch.append(item)
    return batch
```

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Argument Ordering
Write a function `create_dataset(features, labels, batch_size=32, shuffle=True)` that prints:
`Dataset: {features} features, {labels} labels | Batch Size: {batch_size} | Shuffle: {shuffle}`
1. Call this function using only positional arguments.
2. Call this function using only keyword arguments (change the order of parameters in the call).
3. Call this function combining both (pass features and labels positionally, but override `shuffle=False` using a keyword argument).

### Exercise 2: Fixing the Mutable Default Bug
In `practice.py`, you will see a function called `append_to_history`. It is currently broken because it uses `history=[]` as a default.
1. Run the test cases and observe how the history accumulates across calls.
2. Refactor the function to use `None` as the default value, and dynamically create the list inside the function.
3. Verify that the history does not leak between independent calls.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. In Python, why are default argument values evaluated only once at definition time rather than at execution time?
2. If we define a function `def test(a, b=2, c):`, will Python run it? Why or why not?
