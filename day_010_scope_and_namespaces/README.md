# Day 10: Scope, Namespaces, and the LEGB Rule (`global` vs `nonlocal`)

Welcome to Day 10! Today we explore how Python looks up variable names and manages namespaces. Understanding scope is critical for AI Engineers, particularly when managing global training hyperparameters, building stateful data loaders, tracking metrics over training epochs, or designing custom optimization steps.

---

## 🧠 Core Concepts

In Python, a **namespace** is a mapping from names to objects. A **scope** is a textual region of a Python program where a namespace is directly accessible. Python resolves names using the **LEGB Rule**, looking up names in this exact order:

```
  [L] Local Scope     --> Names defined inside the current function
        ↓
  [E] Enclosing Scope --> Names defined inside nested (enclosing) functions
        ↓
  [G] Global Scope    --> Names defined at the top level of the module/file
        ↓
  [B] Built-in Scope  --> Built-in names (e.g., print, len, sum, ValueError)
```

### 1. Global vs. Local Scope and Variable Shadowing
If you define a variable with the same name inside a function as one in the global scope, the local variable **shadows** the global one.
If you want to *modify* a global variable inside a function, you must explicitly declare it using the `global` keyword.

```python
lr = 0.01  # Global variable

def update_learning_rate():
    # Without 'global', Python treats 'lr' as a new local variable
    global lr
    lr = 0.001
```
> [!WARNING]
> While `global` exists, modifying global state inside functions makes code harder to debug, test, and parallelize. Use it sparingly, especially in large ML codebases.

### 2. Enclosing Scope and `nonlocal`
When you have nested functions, the inner function can read variables from the outer (enclosing) function. However, if the inner function needs to *modify* a variable in the enclosing scope, it must use the `nonlocal` keyword.

```python
def make_counter():
    count = 0  # Enclosing scope variable
    
    def counter():
        nonlocal count  # Tells Python to use 'count' from make_counter
        count += 1
        return count
        
    return counter
```
This is the foundation of **Closures**, which we will explore further tomorrow!

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Modifying Global Hyperparameters
During training, we often decay the learning rate.
1. Define a global variable `learning_rate = 0.01`.
2. Write a function `decay_learning_rate(decay_factor)` that:
   - Modifies the global `learning_rate` by multiplying it by `decay_factor`.
   - Returns the updated learning rate.
3. Test your function to verify that calling it updates the global variable.

### Exercise 2: Stateful Exponential Moving Average (EMA) Loss Tracker
When logging training metrics, we often track the Exponential Moving Average (EMA) of the loss to smooth out noise.
The formula is:
$$\text{EMA}_{\text{new}} = (\beta \times \text{EMA}_{\text{old}}) + (1 - \beta) \times \text{current\_loss}$$
1. Write a function `create_ema_tracker(beta)` that defines `ema_loss = None` inside its scope.
2. Inside `create_ema_tracker`, define a nested function `track_loss(current_loss)` that:
   - Accesses and updates `ema_loss` using the `nonlocal` keyword.
   - If `ema_loss` is `None` (first step), set it equal to `current_loss`.
   - Otherwise, update `ema_loss` using the formula above.
   - Returns the updated `ema_loss`.
3. `create_ema_tracker` should return the nested `track_loss` function.

### Exercise 3: Config Shadowing & LEGB Check
Verify how Python resolves overlapping variable names.
1. Write a function `train_model(epochs)` that has a local variable `batch_size = 32`.
2. Inside `train_model`, define a nested function `run_epoch()` that:
   - Prints the current `batch_size` and the global `model_name` (defined outside at the file level).
3. Verify that `run_epoch` successfully accesses the local variable of the parent scope and the global variable.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. What is the difference between `global` and `nonlocal`? What happens if you try to use `nonlocal` on a variable defined in the global scope?
2. What is "variable shadowing"? Why can shadowing built-in functions (like defining a variable named `sum = [1, 2]`) be dangerous in Python?
