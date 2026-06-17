# Day 7: Nested Loops & The Break Trap - Practice Template

# ==========================================
# Exercise 1: Drawing a Grid
# ==========================================

print("--- Exercise 1: Star Grid ---")

# TODO: Write nested loops to print a 4x4 grid of '*' stars.
for row in range(4):
    for col in range(4):
            print ("*",end= " ")
    print()



# Output should look like:
# * * * *
# * * * *
# * * * *
# * * * *


# ==========================================
# Exercise 2: Searching a 2D Matrix
# ==========================================

print("\n--- Exercise 2: Searching 2D Matrix ---")

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

def search_matrix(matrix, target):
    # TODO: Loop through the matrix (use indices for rows and columns).
    for r in range(len(matrix)): # Loop over row index
        for c in range(len(matrix[r])): # Loop over column index on r
            val = matrix [r][c]
            if val == target:
                # print([r][c]) # Don't use print here and [r][c] cannot be used
                return (r,c)
    return None


    # Return (row_idx, col_idx) if found.
    # Return None if the target is not in the matrix.

# Test cases:
print("Search for 11:", search_matrix(matrix, 11))
#print("Search for 100:", search_matrix(matrix, 100))
