# Day 4: Conditionals, Ternary Operator & Scope - Practice Template

# ==========================================
# Exercise 1: Ternary Operator Practice
# ==========================================

score = 85

# TODO: Convert the if-elif-else logic from the README into a single chained ternary expression.
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")  # Replace this with your chained ternary expression
print("Grade:", grade)

# TODO: Add comment explaining readability of chained ternaries:
# One liner ternary operator provides all conditions in one line with if and else operators instead of multiple lines codes.

# ==========================================
# Exercise 2: Python's Scope Trap
# ==========================================

threshold = 0.5

# TODO: Write an if-statement that assigns model_version = "v2" if threshold > 0.8
# Then, print model_version outside the block.
# Test with threshold = 0.9 and threshold = 0.5. Observe what happens.

# Write your code here:
#model_version = "v1"         # Method 1 : Default Fallback Value
#if threshold > 0.8:
#    model_version = "v2"
#print (model_version)

if threshold > 0.8:          # Method 2 : Comprehensive Branches
    model_version = "v2"
else:
    model_version = "v1"
print (model_version)
# TODO: Explain what happened when threshold = 0.5, and how to fix it:
# with 0.5, it shows NameError: name 'model_version' is not defined