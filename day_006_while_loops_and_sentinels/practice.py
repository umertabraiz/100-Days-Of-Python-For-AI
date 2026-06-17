# Day 6: While Loops, Flag Variables & Sentinel Values - Practice Solution

# ==========================================
# Exercise 1: Flag-based Interactive Sum
# ==========================================

print("--- Exercise 1: Flag-based Calculator ---")

def run_calculator():
    total_sum = 0
    keep_going = True  # This is your flag variable
    
    while keep_going:
        action = input("Write 'done' to finish or give value: ")
        
        if action == "done":
            keep_going = False
        else:
            # We wrap the numeric conversion in try-except to prevent crashes
            # if the user types something invalid (like "hello").
            try:
                number = float(action)
                total_sum += number
            except ValueError:
                print("Invalid input! Please enter a number or 'done'.")
    return total_sum

#final_result = run_calculator()
#print(f"Calculator_result: {final_result}")

print(f"Calculator_result: {run_calculator()}")
# ==========================================
# Exercise 2: Return Short-circuiting
# ==========================================

print("\n--- Exercise 2: Return Short-circuiting ---")

def contains_even(numbers_list):
    for num in numbers_list:
        if num % 2 == 0:
            return True  # Exits the function and terminates the loop immediately!
            
    return False  # Only reached if the loop finished without finding an even number

# Test cases (uncommented for execution):
print("Contains even [1, 3, 5]:", contains_even([1, 3, 5]))
print("Contains even [1, 4, 7]:", contains_even([1, 4, 7]))
