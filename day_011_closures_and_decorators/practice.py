# Day 11: Functional Abstractions (Closures & Decorators) - Practice Template

import time
import functools


# ==========================================
# Exercise 1: Latency Profiler Decorator
# ==========================================

print("--- Exercise 1: Latency Profiler Decorator ---")

def time_inference(func):
    # TODO: Use @functools.wraps to preserve function metadata
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Record start time
        start_time = time.time()
        # TODO: Execute func and store
        result = func(*args, **kwargs)
        # TODO: Record end time and print duration formatted to 4 decimal places
        end_time = time.time()
        duration = end_time - start_time
        print(f"[TIMING] Function '{func.__name__}' took {duration:.4f} seconds.")
        # TODO: Return function result
        return result
    return wrapper

# Test timing decorator
@time_inference
def model_forward(input_data):
    """Simulates model forward pass inference."""
    time.sleep(0.55)  # Simulate GPU computation delay
    return [0.92, 0.05, 0.03]

print("Output prediction:", model_forward("image_tensor"))
print("Metadata test (Docstring):", model_forward.__doc__)


# ==========================================
# Exercise 2: API Retry Factory
# ==========================================

print("\n--- Exercise 2: API Retry Factory ---")

def retry_api_calls(max_retries=3, initial_delay=1):
    # TODO: Return a decorator
    def decorator(func):
        # TODO: Use @functools.wraps to preserve function metadata
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Loop up to 'max_retries' times
            for attempt in range(max_retries):
            #Try to run func
                try:
                    return func(*args, **kwargs)
                except RuntimeError as error:
            # If a RuntimeError occurs:
                    if attempt == max_retries - 1:
                        raise error
                    else:
                        delay = initial_delay * (2 ** attempt)
            #   Calculate delay = initial_delay * (2 ** attempt)
            #   Print retry status message and sleep for 'delay' seconds
                        print(f"[RETRY] Attempt {attempt + 1} failed ({error}). Retrying in {delay:.1f} seconds...")
                time.sleep(delay)

            # If all retries fail, raise the final exception
        return wrapper
    return decorator

# Counter for tracking failures
failure_count = 0

@retry_api_calls(max_retries=3, initial_delay=0.1)
def query_llm_api(prompt):
    global failure_count
    # Simulate API failing twice before succeeding
    if failure_count < 2:
        failure_count += 1
        raise RuntimeError("OpenAI API Rate Limit Exceeded")
    return f"LLM Response to: {prompt}"

# Test calling the API
print("API Response:", query_llm_api("Summarize training logs"))


# ==========================================
# Exercise 3: Mock Gradient Tracking Toggle
# ==========================================

print("\n--- Exercise 3: Mock Gradient Tracking Toggle ---")

track_gradients = True

def no_grad_sim(func):
    # TODO: Use @functools.wraps to preserve function metadata
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Reference global 'track_gradients' variable
        global track_gradients
        # TODO: Store the original state of 'track_gradients'
        original_state = track_gradients
        # TODO: Set 'track_gradients' to False
        track_gradients = False
        # TODO: In a try...finally block, run the function
        try:
            result = func(*args, **kwargs)
        # TODO: In the finally block, restore 'track_gradients' to original state
        finally:
            track_gradients = original_state
        # TODO: Return result
        return result
    return wrapper

@no_grad_sim
def run_evaluation(test_loader):
    print(f"Evaluating model... [Gradient Tracking Active: {track_gradients}]")
    return 0.965

# Test evaluation toggle
print("Before Eval - Gradient tracking active:", track_gradients)  # Expected: True
eval_acc = run_evaluation("val_set")
print("Evaluation accuracy:", eval_acc)
print("After Eval - Gradient tracking active:", track_gradients)   # Expected: True


# ==========================================
# Answers to Socratic Questions
# ==========================================
# Write your answers below:
# 1- Why is it important to use @functools.wraps inside our decorators?
# To preserve the actual values
# 2- What is the execution order of multiple decorators applied to a single function?
# @time_inference and then @retry_api_calls
