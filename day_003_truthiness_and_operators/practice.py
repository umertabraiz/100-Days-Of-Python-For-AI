# Day 3: Truthiness, Logical Operators & Short-Circuit Evaluation - Practice Template

# ==========================================
# Exercise 1: Exploring Truthiness
# ==========================================

test_values = [None, 0, 42, "", "AI", [], [1, 2], {}, {"model": "Gemini"}]

# TODO: Loop through test_values and print whether each is truthy or falsy using bool()
print("--- Exercise 1: Truthiness ---")
for i in test_values:
    print (i,":", bool(i))

# ==========================================
# Exercise 2: Short-Circuiting Practice
# ==========================================

print("\n--- Exercise 2: Short-Circuiting ---")

# TODO: Print and verify these expressions. Then add comments explaining why they return what they do.
# 1. "" or "Python"
print("" or "Python") # It returns "Python" because python reads it after getting "" as Falsy.
# 2. "Machine Learning" or "Deep Learning"
print ("Machine Learning" or "Deep Learning") # It returns "Machine Learning" because python takes it as Truthy.
# 3. 0 and [1, 2]
print (0 and [1, 2])  # It returns 0 because python reads it after getting 0 as Falsy and does not go to next object because of and operation
# 4. [10] and "TensorFlow"
print ([10] and "TensorFlow") # It returns "TensorFlow" because python jumps towards it after getting [10] as Truthy object because of and operation.

# ==========================================
# Exercise 3: Safe Division (Short-Circuit Guard)
# ==========================================

print("\n--- Exercise 3: Safe Division ---")

# TODO: Implement a one-line expression that divides 100 by denom.
# If denom is 0, return 0 (no ZeroDivisionError should be thrown).
# Test with both denom = 5 and denom = 0.

def safe_divide(denom):
    # Hint: Use short-circuiting logical operators to guard the division.
    result = denom and 100 / denom # TODO: replace this with your one-liner
    return result

print("Divide by 5:", safe_divide(5))
print("Divide by 0:", safe_divide(0))
