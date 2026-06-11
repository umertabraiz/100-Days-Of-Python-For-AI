# Day 2: Dynamic Typing, Mutability & Reference Counting - Practice Template
import sys

# ==========================================
# Exercise 1: Mutability & Memory Addresses
# ==========================================

# 1. Create a list, print its id, modify it, print its id again.
my_list = [1, 2, 3]
print("Initial list:", my_list, "ID:", id(my_list))

# Modify my_list
# TODO: append 4 to my_list
my_list.append(4)
print("Modified list:", my_list, "ID:", id(my_list))

# 2. Create a string, print its id, modify it, print its id again.
my_str = "Hello"
print("Initial string:", my_str, "ID:", id(my_str))

# Modify my_str
# TODO: concatenate " World" to my_str
my_str = "Hello" + " World"
print("Modified string:", my_str, "ID:", id(my_str))

# TODO: Add comments explaining why this difference matters for performance:
# so that we can keep both objects intact in the memory


# ==========================================
# Exercise 2: The Tuple Mutability Loophole
# ==========================================

# 1. Create a tuple containing a list
my_tuple = (1, 2, [3, 4])
print("Initial tuple:", my_tuple)

# 2. Try to change the first element (uncomment the line below to test, then comment it back after seeing the error)
#my_tuple[0] = 100

# 3. Try to modify the list inside the tuple
# TODO: append 5 to the list inside my_tuple
my_tuple[2].append(5)
print("Tuple after modifying the inner list:", my_tuple)

# TODO: Explain why this is possible: Because the modification was directly done within list which is mutable


# ==========================================
# Exercise 3: Reference Counting Investigation
# ==========================================

# 1. Create a reference to a new object
a = [999] * 1000

# 2. Check reference count (remember sys.getrefcount adds 1)
# TODO: print the reference count of 'a'
#print(sys.getrefcount(a))
# 3. Create more references and check ref count
# TODO: create b and c referencing a, then print ref count of 'a'
b = a
c = a
print(sys.getrefcount(a))
# 4. Delete reference and check ref count
# TODO: delete b, then print ref count of 'a'
del b
print(sys.getrefcount(a))