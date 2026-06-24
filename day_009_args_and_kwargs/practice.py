# Day 9: Arbitrary Arguments (*args and **kwargs) - Practice Template

# ==========================================
# Exercise 1: Custom Math Pipeline (*args)
# ==========================================

print("--- Exercise 1: Custom Math Pipeline ---")

def multiply_and_sum(multiplier, *numbers):
    # Multiply each number in the 'numbers' tuple by 'multiplier'
    multiplied = [n * multiplier for n in numbers]
    # Return the sum of these results.
    return sum(multiplied)

# Test cases:
print("Result 1:", multiply_and_sum(2, 1, 2, 3))  # Expected: 12
print("Result 2:", multiply_and_sum(5))           # Expected: 0


# ==========================================
# Exercise 2: AI Model Logger (**kwargs)
# ==========================================

print("\n--- Exercise 2: AI Model Logger ---")

def log_metrics(model_name, **metrics):
    # Print: "[LOG - {model_name}]"
    print(f"[LOG - {model_name}]")
    # Loop through metrics, uppercase the key name, and print "- KEY: VALUE"
    for key, value in metrics.items():
        print(f"- {key.upper()}: {value}")


# Test call:
log_metrics("GPT-4", loss=0.12, accuracy=0.98, step=1000)


# ==========================================
# Exercise 3: Config Unpacking
# ==========================================

print("\n--- Exercise 3: Config Unpacking ---")

def build_nn(input_size, hidden_size, output_size):
    print(f"NN Architecture -> Input: {input_size} | Hidden: {hidden_size} | Output: {output_size}")

nn_config = {"input_size": 30, "hidden_size": 20, "output_size": 10}
# TODO: Create a dictionary called nn_config with keys: 'input_size', 'hidden_size', 'output_size'
# Then, call build_nn by unpacking the dictionary.
build_nn(**nn_config)