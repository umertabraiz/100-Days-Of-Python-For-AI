# Day 9: Arbitrary Arguments (*args and **kwargs) & Unpacking

Welcome to Day 9! Today we dive into one of Python's most powerful and dynamic features: **`*args` and `**kwargs`**. 

If you look at the source code of any major AI framework like PyTorch, Hugging Face Transformers, or LangChain, you will see `*args` and `**kwargs` used everywhere. They allow functions to accept any number of inputs and pass configurations dynamically through helper classes.

---

## 🧠 Core Concepts

### 1. `*args`: Variable Positional Arguments
The single asterisk `*` gathers any extra positional arguments passed to the function into a **tuple**.

```python
def add_all(*args):
    # args is a tuple, e.g., (1, 2, 3)
    print(f"Arguments tuple: {args}")
    return sum(args)

print(add_all(1, 2, 3, 4))  # Outputs: 10
```

### 2. `**kwargs`: Variable Keyword Arguments
The double asterisk `**` gathers any extra keyword arguments passed to the function into a **dictionary**.

```python
def print_model_config(**kwargs):
    # kwargs is a dictionary, e.g., {"lr": 0.01, "batch_size": 32}
    print(f"Config dict: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_model_config(lr=0.001, optimizer="Adam", epochs=10)
```

### 3. Argument Unpacking (The Reverse Asterisk)
You can also use `*` and `**` to **unpack** lists/tuples and dictionaries when *calling* a function.

```python
def setup_hyperparameters(learning_rate, epochs, batch_size):
    print(f"LR: {learning_rate} | Epochs: {epochs} | Batch Size: {batch_size}")

config_dict = {"learning_rate": 0.001, "epochs": 15, "batch_size": 64}

# Instead of passing them individually, we unpack the dictionary!
setup_hyperparameters(**config_dict)
```

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Custom Math Pipeline (*args)
Write a function `multiply_and_sum(multiplier, *numbers)` that:
1. Multiplies each number in the `numbers` tuple by the `multiplier`.
2. Returns the sum of all the multiplied numbers.
3. Test cases:
   - `multiply_and_sum(2, 1, 2, 3)` ➔ Should calculate $(2\times1) + (2\times2) + (2\times3) = 12$.
   - `multiply_and_sum(5)` ➔ Should return `0` (since `numbers` is empty).

### Exercise 2: AI Model Logger (**kwargs)
When training ML models, we want to log dynamic metrics (like loss, accuracy, epoch) dynamically.
1. Write a function `log_metrics(model_name, **metrics)` that:
   - Prints: `"[LOG - {model_name}]"`
   - Loops through the `metrics` dictionary and prints each metric in uppercase, formatted as: `"- METRIC: VALUE"` (e.g. `"- ACCURACY: 0.95"`).
2. Test it by calling it with:
   `log_metrics("GPT-4", loss=0.12, accuracy=0.98, step=1000)`

### Exercise 3: Config Unpacking
1. Define a function `build_nn(input_size, hidden_size, output_size)`. It should just print the parameters.
2. Create a dictionary `nn_config` containing values for these three parameters.
3. Call `build_nn` by **unpacking** the `nn_config` dictionary.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. In `multiply_and_sum(multiplier, *numbers)`, why does the parameter `multiplier` have to come *before* `*numbers`? What would happen if we wrote `*numbers, multiplier`?
2. What is the type of the variable `args` inside a function? What is the type of `kwargs`?
