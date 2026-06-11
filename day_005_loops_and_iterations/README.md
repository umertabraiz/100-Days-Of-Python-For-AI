# Day 5: Loops, Iteration & Loop-Else Clauses

Welcome to Day 5! Today, you will master Python's loop control structures (`for` and `while`), learn how to control loop flow using `break`, `continue`, and `pass`, and explore one of Python's most unique (and often misunderstood) features: the **loop `else` clause**.

---

## 🧠 Core Concepts

### 1. `for` Loops vs. `while` Loops
- **`for` loop**: Used when you want to iterate over a pre-determined sequence (like a list, string, range, or database query result).
  ```python
  for i in range(3):
      print(i)
  ```
- **`while` loop**: Used when you want to repeat code until a specific condition becomes false.
  ```python
  count = 0
  while count < 3:
      print(count)
      count += 1
  ```

### 2. Loop Control: `break`, `continue`, and `pass`
- **`break`**: Terminates the loop immediately. Execution jumps to the statement after the loop.
- **`continue`**: Skips the rest of the current iteration and jumps to the next cycle of the loop.
- **`pass`**: A null statement. It does absolutely nothing. Used as a placeholder where syntax requires a statement (e.g., in empty loops, functions, or classes).

### 3. The Loop-`Else` Clause: Python's Hidden Feature
In Python, both `for` and `while` loops can have an optional `else` block. 
* **The `else` block executes ONLY IF the loop completes naturally** (without encountering a `break` statement).
* If the loop is terminated by a `break`, the `else` block is **skipped**.

Think of loop-`else` as a **"no-break"** clause. It is incredibly useful for search operations where you want to execute code only if the item was *not* found.

#### 🔍 Socratic Experiment: Loop-Else Search
Predict what this outputs:
```python
items = [1, 3, 5, 7]
target = 4

for item in items:
    if item == target:
        print("Found target!")
        break
else:
    print("Target not found.")
```

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Controlling the Flow
Write a script that:
1. Loops through numbers from `1` to `20` (inclusive).
2. If the number is divisible by `5`, skip it using `continue`.
3. If the number is `17`, stop the loop entirely using `break`.
4. Print the numbers that make it through.

### Exercise 2: AI Input Validator (Loop-Else Pattern)
In AI systems, you often need to validate incoming payloads (e.g., checking if prompt text contains forbidden words).
1. Create a list of forbidden words: `forbidden = ["spam", "hack", "bypass"]`.
2. Write a prompt validator that takes user input text (e.g., `"How to bypass the API restrictions"`).
3. Split the text into words. Loop through the words.
4. If a word matches any in the `forbidden` list, print `"Prompt rejected: contains unsafe word!"` and `break` out of the loop.
5. Use a loop-`else` clause to print `"Prompt approved: prompt is clean."` if no forbidden words were found.
6. Test it with both clean and forbidden inputs.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. In Exercise 2, why is using loop-`else` cleaner than using a boolean flag like `is_clean = True`?
2. What is the difference between `pass` and `continue` inside a loop?
