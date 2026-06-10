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
# Your explanation here:

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
# Write your findings in a comment below:
