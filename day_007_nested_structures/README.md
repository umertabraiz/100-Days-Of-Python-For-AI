# Day 7: Nested Loops & The Break Trap

Welcome to Day 7! Today, we conclude our Control Flow segment by going nested. In AI engineering, data is rarely 1-dimensional. Whether you are processing a grid of image pixels, batches of tokens, or coordinates in a dataset, you will constantly write **nested loops** (loops inside loops).

Today, we will master how to iterate through 2D structures and learn a critical control-flow rule: **how `break` behaves in nested loops**.

---

## 🧠 Core Concepts

### 1. Nested Loops (2D Iteration)
When you run a loop inside another loop, the **inner loop** runs to completion for every single iteration of the **outer loop**.

```python
# Iterating through coordinates (row, col)
for row in range(2):       # Outer loop
    for col in range(3):   # Inner loop
        print(f"({row}, {col})")
```
Output:
```text
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
```

### 2. The Inner-Loop Break Trap
A very common bug is expecting `break` to stop all execution. 
In Python, **`break` only exits the innermost loop that contains it.** The outer loop will continue running!

```python
# The Break Trap
for row in range(3):
    for col in range(3):
        if col == 1:
            break  # Exits only the 'col' loop!
        print(f"Row {row}, Col {col}")
```
Output:
```text
Row 0, Col 0
Row 1, Col 0
Row 2, Col 0
```
*(Notice that even though we broke, the loop moved on to Row 1 and Row 2. The outer loop kept going!)*

### 3. How to Break Out of Both Loops
If you want to stop the entire operation when a condition is met in an inner loop, you have two main patterns:

#### Pattern A: The Flag Variable (Clean & Standard)
Use a boolean flag to tell the outer loop to stop.
```python
stop_all = False
for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            stop_all = True
            break  # Break inner loop
    if stop_all:
        break  # Break outer loop
```

#### Pattern B: Function Return (Elegantly Short-circuit)
If you wrap your loops inside a function, calling `return` immediately exits both loops and the entire function. **This is usually the cleanest code pattern.**
```python
def find_coordinates():
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                return (row, col)  # Exits everything instantly
```

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Drawing a Grid (Nested Loops)
Let's practice mechanical loop iteration by drawing patterns (common interview task for logic testing).
Write a script that uses nested `for` loops to print a 4x4 grid of stars like this:
```text
* * * *
* * * *
* * * *
* * * *
```
*Hint: You can use `print("*", end=" ")` to print a star and a space without starting a new line, and a blank `print()` at the end of the inner loop to start a new row.*

### Exercise 2: Searching a 2D Matrix (Function Exit)
In AI, matrices are used to store data. Let's write a search algorithm for a 2D list (a list of lists).
1. Given this matrix:
   ```python
   matrix = [
       [1, 3, 5],
       [7, 9, 11],
       [13, 15, 17]
   ]
   ```
2. Write a function `search_matrix(matrix, target)` that loops through the rows and columns.
3. If it finds the `target` value, it should immediately **`return`** the location as a tuple `(row_index, col_index)`.
4. If the entire matrix is searched and the target is not found, **`return None`**.
5. Test it searching for `11` (should return `(1, 2)`) and `100` (should return `None`).

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. In Exercise 2, why did we use `return` instead of `break` to exit the nested loops when we found the target?
2. If we had used `break` in Exercise 2 instead of `return`, what would have happened to the search?
