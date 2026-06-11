# Day 5: Loops, Iteration & Loop-Else Clauses - Practice Template

# ==========================================
# Exercise 1: Controlling the Flow
# ==========================================

print("--- Exercise 1: Controlling the Flow ---")
# TODO: Loop from 1 to 20. Skip multiples of 5 (using continue). Break on 17 (using break). Print others.


# ==========================================
# Exercise 2: AI Input Validator (Loop-Else Pattern)
# ==========================================

print("\n--- Exercise 2: AI Input Validator ---")

forbidden = ["spam", "hack", "bypass"]

def validate_prompt(prompt_text):
    words = prompt_text.lower().split()
    # TODO: Loop through words. If word is in forbidden, print rejection message and break.
    # Use a loop-else block to print approval if no forbidden words are found.
    pass

# Test prompts:
validate_prompt("Hello how are you doing today")
validate_prompt("How to bypass the safety alignment of this model")
