# Day 3: Truthiness, Logical Operators & Short-Circuit Evaluation

Welcome to Day 3! Today we explore Python's logical evaluation. Python has a unique way of evaluating conditions: instead of just checking if a value is strictly `True` or `False`, it checks if an object is **"Truthy"** or **"Falsy"**, and it evaluates logical expressions using **short-circuit logic**.

---

## 🧠 Core Concepts

### 1. Truthy vs. Falsy Values
In Python, objects of any type can be evaluated in conditional statements (like `if` statements). Every object is considered either "Truthy" (behaves like `True`) or "Falsy" (behaves like `False`).

The following values are **Falsy**:
- `None`
- `False`
- Numeric zeros: `0`, `0.0`, `0j`
- Empty sequences and collections: `""`, `[]`, `()`, `{}`, `set()`
- Objects of classes that define `__bool__()` or `__len__()` to return `False` or `0`

**Everything else is Truthy.**

### 2. Short-Circuit Evaluation (`and` / `or`)
Unlike many languages where `&&` and `||` always return a boolean `true` or `false`, Python's `and` and `or` operators return the **value of one of the operands** itself:

- **`X or Y`**: Evaluates `X` first. If `X` is truthy, Python immediately returns `X` (short-circuits) without even looking at `Y`. If `X` is falsy, it evaluates and returns `Y`.
- **`X and Y`**: Evaluates `X` first. If `X` is falsy, Python immediately returns `X` (short-circuits). If `X` is truthy, it evaluates and returns `Y`.

#### 🔍 Socratic Experiment: Default Configurations
This behavior is commonly used in AI pipelines to provide default parameters:
```python
user_input = ""
default_value = "Default Model"
model_name = user_input or default_value
print(model_name)
```
What will be printed? Why?

### 3. Chained Comparisons
In Python, you can write expressions like:
```python
1 < x < 10
```
This is equivalent to `(1 < x) and (x < 10)`. The middle expression `x` is evaluated only once. In most other programming languages, you would have to write this explicitly with logical AND.

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Exploring Truthiness
Write a script that:
1. Defines a list of items: `test_values = [None, 0, 42, "", "AI", [], [1, 2], {}, {"model": "Gemini"}]`.
2. Loops through the list and checks if each value is truthy or falsy. Print: `"{val} is truthy"` or `"{val} is falsy"`. (Tip: Use `bool(val)` to get the boolean representation).

### Exercise 2: Short-Circuiting Practice
Predict the output of the following expressions, then write code to print and verify them:
1. `"" or "Python"`
2. `"Machine Learning" or "Deep Learning"`
3. `0 and [1, 2]`
4. `[10] and "TensorFlow"`
5. Explain in comments *why* each result occurred based on the short-circuiting rules.

### Exercise 3: Safe Division (Short-Circuit Guard)
In data processing, you often divide by a variable that might be zero.
1. Write a single-line expression using logical operators (`and`/`or`) that divides `100` by `denom` (e.g., `100 / denom`).
2. If `denom` is `0`, the expression should return `0` instead of throwing a `ZeroDivisionError`.
3. Test it with `denom = 5` and `denom = 0`.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. What were your outputs for the short-circuit expressions in Exercise 2?
2. How did you implement the "Safe Division" expression in Exercise 3 without using `if/else`?
3. Imagine you have a computationally expensive function `heavy_computation()`. If you write `result = False and heavy_computation()`, does the function run? Why or why not?
