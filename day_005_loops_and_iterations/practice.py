# Day 5: Loops, Iteration & Loop-Else Clauses - Practice Template

# ==========================================
# Exercise 1: Controlling the Flow
# ==========================================

print("--- Exercise 1: Controlling the Flow ---")
# TODO: Loop from 1 to 20. Skip multiples of 5 (using continue). Break on 17 (using break). Print others.

for i in range(1,21):
    if i % 5 == 0:
        continue
    elif i == 17:
        break
    print(i)





# ==========================================
# Exercise 2: AI Input Validator (Loop-Else Pattern)
# ==========================================

print("\n--- Exercise 2: AI Input Validator ---")

forbidden = ["spam", "hack", "bypass"]

def validate_prompt(prompt_text):
    words = prompt_text.lower().split()
    # TODO: Loop through words. If word is in forbidden, print rejection message and break.
    # Use a loop-else block to print approval if no forbidden words are found.
    for word in words:
        if word in forbidden:
            print("Prompt rejected: contains unsafe word!")
            break
    else:
        print("Prompt approved: prompt is clean.")

# Test prompts:
#validate_prompt("Hello how are you doing today")
validate_prompt("How to bypass the safety alignment of this model")
