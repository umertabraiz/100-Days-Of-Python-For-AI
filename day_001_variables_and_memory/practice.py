# Day 1: Python Memory Model & Variables - Practice Template

# ==========================================
# Exercise 1: Object Identity Challenge
# ==========================================

# 1. Create list1 and list2 with values [10, 20, 30]
list1 = [10, 20, 30]
list2 = [10, 20, 30]

# 2. Compare using '==' and 'is'
print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)

# 3. Add comment explaining the difference:
# - '==' compares the VALUES of the objects (equality). Both lists contain [10, 20, 30], so this is True.
# - 'is' compares the IDENTITIES (memory addresses) of the objects (reference/identity).
#   Since list1 and list2 are two separate lists created at different memory addresses, this is False.

# 4. Append 40 to list1 and check list2
list1.append(40)
print("list1 after append:", list1)
print("list2 after append:", list2)

# 5. Create list3 = list1, compare them, modify list3, check list1
list3 = list1
print("list1 == list3:", list1 == list3)
print("list1 is list3:", list1 is list3)

list3.append(50)
print("list1 after list3 modification:", list1)
print("list3 after modification:", list3)


# ==========================================
# Exercise 2: The Integer Caching Mystery
# ==========================================

# 1. Compare x = 256 and y = 256 using 'is'
x1 = 256
y1 = 256
print("256: x1 is y1:", x1 is y1)

# 2. Compare x = 257 and y = 257 using 'is'
x2 = 257
y2 = 257
print("257: x2 is y2:", x2 is y2)

# 3. Run this file using 'python practice.py' and compare it with running line-by-line in the REPL.
# Findings:
# - In a script (like python practice.py), Python compiles the entire block of code at once.
#   The compiler optimizes memory by reusing identical integer literals (like 257) within the same block,
#   so both x2 and y2 point to the same memory location, making 'x2 is y2' True.
# - In an interactive REPL, each line is compiled separately. Python's global integer caching
#   (interning) only pre-allocates integers from -5 to 256. Since 257 is outside this range,
#   in the REPL, x2 and y2 are created as separate objects, making 'x2 is y2' False.
