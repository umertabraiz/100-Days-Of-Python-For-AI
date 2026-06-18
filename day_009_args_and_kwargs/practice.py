# Day 9: Arbitrary Arguments (*args and **kwargs) - Practice Template

# ==========================================
# Exercise 1: Custom Math Pipeline (*args)
# ==========================================

print("--- Exercise 1: Custom Math Pipeline ---")

def multiply_and_sum(multiplier, *numbers):
    # TODO: Multiply each number in the 'numbers' tuple by 'multiplier'
    # Return the sum of these results.
    pass

# Test cases:
# print("Result 1:", multiply_and_sum(2, 1, 2, 3))  # Expected: 12
# print("Result 2:", multiply_and_sum(5))           # Expected: 0


# ==========================================
# Exercise 2: AI Model Logger (**kwargs)
# ==========================================

print("\n--- Exercise 2: AI Model Logger ---")

def log_metrics(model_name, **metrics):
    # TODO: Print: "[LOG - {model_name}]"
    # Loop through metrics, uppercase the key name, and print "- KEY: VALUE"
    pass

# Test call:
# log_metrics("GPT-4", loss=0.12, accuracy=0.98, step=1000)


# ==========================================
# Exercise 3: Config Unpacking
# ==========================================

print("\n--- Exercise 3: Config Unpacking ---")

def build_nn(input_size, hidden_size, output_size):
    print(f"NN Architecture -> Input: {input_size} | Hidden: {hidden_size} | Output: {output_size}")

# TODO: Create a dictionary called nn_config with keys: 'input_size', 'hidden_size', 'output_size'
# Then, call build_nn by unpacking the dictionary.
