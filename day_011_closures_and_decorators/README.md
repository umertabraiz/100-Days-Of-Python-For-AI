# Day 11: Functional Abstractions (Closures & Decorators)

Welcome to Day 11! Today we explore **Closures** and **Decorators**—two of Python's most elegant functional paradigms. As an AI Engineer, you will encounter these patterns constantly:
- **Framework Optimization**: Disabling gradient tracking (`@torch.no_grad()`) or compiling subgraphs (`@tf.function`).
- **Web App Routing**: Defining endpoints in FastAPI (`@app.post("/predict")`).
- **Production Safety**: Adding logging, performance timers, or retry logic when querying external APIs like OpenAI, Anthropic, or Hugging Face.

---

## 🧠 Core Concepts

### 1. Closures: Preserving Enclosing State
A closure is a nested function that **remembers and has access to variables from its enclosing scope**, even after the outer function has finished executing.

```python
# The outer function creates a customized multiplier function
def make_multiplier(factor):
    # The inner function is a closure that captures the 'factor' variable from the parent scope
    def multiplier(number):
        # It references 'factor' which was defined when make_multiplier was called
        return number * factor
    return multiplier  # Returns the inner function object

double = make_multiplier(2)  # Creates a function that doubles numbers (factor=2 is saved in the closure)
print(double(5))  # Outputs: 10 (calls multiplier(5), which calculates 5 * 2)
```

### 2. Decorators: Wrapping Function Behavior
A decorator is a function that takes another function as an argument, extends its behavior without modifying it, and returns the modified function.

```python
# The decorator function accepts the target function 'func' as an argument
def log_execution(func):
    # The wrapper function takes any number of positional (*args) and keyword (**kwargs) arguments
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")  # Prints the name of the function before it runs
        result = func(*args, **kwargs)      # Executes the original function and captures its return value
        print(f"Finished: {func.__name__}") # Prints the name after execution finishes
        return result                       # Returns the captured output so the function works normally
    return wrapper  # Returns the wrapper function object to replace the original function

@log_execution  # Equivalent to: train_step = log_execution(train_step)
def train_step():
    print("Executing backpropagation...")
```

### 3. Preserving Metadata: `functools.wraps`
When wrapping a function, the wrapper function replaces the original function. Consequently, metadata like the original name (`__name__`) and docstring (`__doc__`) are lost. To prevent this, we use the `@functools.wraps` decorator.

```python
import functools

# A decorator that preserves the original function's name and documentation
def safe_decorator(func):
    # @functools.wraps is a built-in decorator that copies metadata (like __name__ and __doc__)
    # from the original function 'func' onto our new 'wrapper' function.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)  # Executes and returns the original function
    return wrapper  # Returns the decorated wrapper
```

### 4. Decorator Factories (Decorators with Arguments)
To pass arguments to a decorator itself, you need an extra layer of nesting: a function that returns a decorator.

```python
# The outer function is the 'Decorator Factory' that receives the configuration arguments
def repeat(times):
    # This middle function is the actual decorator that receives the target function
    def decorator(func):
        # This inner function is the wrapper that intercepts the call to 'func'
        # *args and **kwargs collect any positional and keyword arguments passed to print_hello
        def wrapper(*args, **kwargs):
            # 'range(times)' creates a sequence of numbers of length 'times' (e.g., if times=3, it's [0, 1, 2])
            # The underscore '_' is a throwaway variable name in Python. It is used when we need to loop
            # a specific number of times but we do not actually care about the loop index value (0, 1, or 2).
            for _ in range(times):
                func(*args, **kwargs)  # Calls the original function with its original arguments
        return wrapper  # Returns the customized wrapper function
    return decorator  # Returns the decorator configured with 'times'

# Applying the decorator with the argument times=3
@repeat(times=3)
def print_hello():
    print("Hello")
```

---

## 🛠️ Exercises for Today

Open `practice.py` in this directory and solve these exercises:

### Exercise 1: Latency Profiler Decorator (`@time_inference`)
When deploying ML models to production, monitoring the latency of model inference is vital.
1. Write a decorator named `time_inference(func)` that measures the execution time of a function.
2. It should:
   - Use `@functools.wraps(func)` to preserve metadata.
   - Record the start time before calling `func`.
   - Call `func` and store its result.
   - Record the end time and print the elapsed duration formatted as: `"[TIMING] Function '{func.__name__}' took X.XXXX seconds."`
   - Return the result of the function call.
3. Test it on a simulated `model_forward(input_data)` function.

### Exercise 2: API Retry Factory (`@retry_api_calls`)
External API connections (like querying OpenAI or Hugging Face APIs) often fail due to network glitches or rate limits. A robust pipeline should automatically retry failed requests with an **exponential backoff delay**.
1. Write a decorator factory `retry_api_calls(max_retries=3, initial_delay=1)` that returns a decorator.
2. The wrapper should:
   - Attempt to call the decorated function.
   - If a `RuntimeError` is caught, increment the retry counter and calculate a backoff delay:
     $$\text{delay} = \text{initial\_delay} \times (2^{\text{attempt}})$$
   - Sleep for the calculated delay, print a retry log: `"[RETRY] Attempt X failed. Retrying in Y seconds..."`, and try again.
   - If the retries are exhausted, raise the final exception.
3. Test your decorator on a mock `query_llm_api()` function that randomly fails.

### Exercise 3: Mock Gradient Tracking Toggle (`@no_grad_sim`)
PyTorch uses the `@torch.no_grad()` decorator to temporarily disable gradient computations, saving memory during model evaluation.
1. Define a global variable `track_gradients = True`.
2. Write a decorator `no_grad_sim(func)` that:
   - Stores the original value of the global `track_gradients` variable.
   - Temporarily sets `track_gradients = False`.
   - Executes the decorated function inside a `try...finally` block.
   - Restores `track_gradients` to its original value in the `finally` block (ensuring the state is restored even if the function errors).
   - Returns the result of the function.
3. Verify that gradient tracking is successfully turned off during evaluation, and turns back on afterwards.

---

## 💬 Socratic Discussion
Once you complete `practice.py`, answer:
1. Why is it important to use `@functools.wraps` inside our decorators? What metadata is lost if we don't?
2. What is the execution order of multiple decorators applied to a single function (e.g., placing `@time_inference` and `@retry_api_calls` on the same function)? Which wrapper runs first?
