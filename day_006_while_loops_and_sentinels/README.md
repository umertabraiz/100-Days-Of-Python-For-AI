# Day 6: While Loops, Flag Variables & Sentinel Values

Welcome to Day 6! Based on our transition to a **Dynamic Adaptive Curriculum**, we are slowing down to build a deep foundation in **loop state control, function return values, and flag variables**. 

Before moving to complex structures, you must become fully comfortable with how loops interact with functions and memory.

---

## 🧠 Core Concepts

### 1. The "Flag Variable" Pattern
In programming, a **flag** is a boolean variable (`True` or `False`) used as a signal to keep track of a state. 

While Python's loop-`else` is a nice shorthand, the **flag variable pattern** is the universal standard across almost all programming languages (C, C++, Java, JavaScript, Go). It is vital to master this pattern because you will see it in almost every production codebase.

```python
# The Flag Pattern
is_running = True  # The flag

while is_running:
    action = input("Type 'stop' to end: ")
    if action == "stop":
        is_running = False  # Changing the flag to exit the loop next iteration
```

### 2. Return vs. Print inside Functions
A very common trap for beginners is using `print()` inside a function instead of `return`.
* **`print()`** just displays a message on the screen. The computer cannot use that message for further calculations.
* **`return`** exits the function and hands a value back to the caller. 

```python
def add_print(a, b):
    print(a + b)  # Displays the sum, returns None

def add_return(a, b):
    return a + b  # Returns the sum to be used elsewhere

# Test
x = add_print(5, 5)   # x is None
y = add_return(5, 5)  # y is 10
print(y * 2)          # Outputs 20
```

### 3. Sentinel Values in Loops
A **sentinel value** is a special value that signals the loop to terminate (like typing `'exit'` or `'done'`).

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: flag-based Interactive Sum
Write a function `run_calculator()` that:
1. Uses a flag variable `keep_going = True` to control a `while` loop.
2. Inside the loop, prompts the user: `Enter a number to add to the sum (or type 'done' to finish): `.
3. If the user enters `'done'`, set the flag `keep_going = False` to stop the loop.
4. If they enter a number, add it to a running total.
5. If they enter anything else, print `"Invalid input, try again"` and do not add it to the sum.
6. The function should **`return`** the final sum (do not just print it inside the function!).

### Exercise 2: Loop Flag vs. Return Short-circuiting
Did you know that inside a function, calling `return` immediately terminates the function **and** any loops running inside it?
1. Write a function `contains_even(numbers_list)` that takes a list of integers.
2. Loop through the list. As soon as you find an even number, **`return True`** immediately. (This short-circuits the loop and function).
3. If the loop completes and no even number was found, **`return False`**.
4. Observe how you don't even need a `break` statement because `return` does it automatically.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. In Exercise 2, what happens to the remaining elements in the list if the first element is even? Does the loop continue checking them?
2. If a function does not have a `return` statement, what does it return by default in Python?
