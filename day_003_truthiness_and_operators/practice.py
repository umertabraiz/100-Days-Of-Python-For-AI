# Day 3: Truthiness, Logical Operators & Short-Circuit Evaluation - Practice Template

# ==========================================
# Exercise 1: Exploring Truthiness
# ==========================================

test_values = [None, 0, 42, "", "AI", [], [1, 2], {}, {"model": "Gemini"}]

# TODO: Loop through test_values and print whether each is truthy or falsy using bool()
print("--- Exercise 1: Truthiness ---")


# ==========================================
# Exercise 2: Short-Circuiting Practice
# ==========================================

print("\n--- Exercise 2: Short-Circuiting ---")

# TODO: Print and verify these expressions. Then add comments explaining why they return what they do.
# 1. "" or "Python"
# 2. "Machine Learning" or "Deep Learning"
# 3. 0 and [1, 2]
# 4. [10] and "TensorFlow"


# ==========================================
# Exercise 3: Safe Division (Short-Circuit Guard)
# ==========================================

print("\n--- Exercise 3: Safe Division ---")

# TODO: Implement a one-line expression that divides 100 by denom.
# If denom is 0, return 0 (no ZeroDivisionError should be thrown).
# Test with both denom = 5 and denom = 0.

def safe_divide(denom):
    # Hint: Use short-circuiting logical operators to guard the division.
    result = None # TODO: replace this with your one-liner
    return result

print("Divide by 5:", safe_divide(5))
print("Divide by 0:", safe_divide(0))
