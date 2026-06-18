# Day 8: Functions, Arguments & The Mutable Default Trap - Practice Template

# ==========================================
# Exercise 1: Argument Ordering
# ==========================================

print("--- Exercise 1: Argument Ordering ---")

# TODO: Define create_dataset(features, labels, batch_size=32, shuffle=True)
# Have it print: f"Dataset: {features} features, {labels} labels | Batch Size: {batch_size} | Shuffle: {shuffle}"
def create_dataset(features, labels, batch_size=32, shuffle=True):
    print(f"Dataset: {features} features, {labels} labels | Batch Size: {batch_size} | Shuffle: {shuffle}")
create_dataset("red, white, black", "color" )
#create_dataset(batch_size=32, shuffle=True, features="red, white, black", labels="color")
#create_dataset("red, white, black", "color", shuffle=False,batch_size=30)
# TODO: Test cases
# 1. Call positionally
# 2. Call with keywords in mixed order
# 3. Call mixed (positional + keyword override)


# ==========================================
# Exercise 2: Fixing the Mutable Default Bug
# ==========================================

print("\n--- Exercise 2: Fixing Mutable Defaults ---")

# Broken function (uses mutable default list)
def append_to_history(action, history=[]):
    history.append(action)
    return history

# Demonstrating the bug:
print("Call 1:", append_to_history("Started Model Training"))
print("Call 2:", append_to_history("Loaded Weights"))  # Notice weights gets added to Call 1's list!

# TODO: Refactor the function below to fix the bug using the 'None' pattern:
def append_to_history_fixed(action, history=None):
    if history is None:
        history =[]

    history.append(action)
    return history

# Test the fixed function:
print("Fixed Call 1:", append_to_history_fixed("Started Model Training"))
print("Fixed Call 2:", append_to_history_fixed("Loaded Weights"))
