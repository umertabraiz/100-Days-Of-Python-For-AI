# Day 10: Scope, Namespaces, and the LEGB Rule - Practice Template

# ==========================================
# Exercise 1: Modifying Global Hyperparameters
# ==========================================

print("--- Exercise 1: Global Hyperparameter Decay ---")

learning_rate = 0.01

def decay_learning_rate(decay_factor):
    # TODO: Declare the use of the global 'learning_rate' variable
    global learning_rate
    learning_rate = decay_factor * learning_rate
    return learning_rate


    # Modify it by multiplying it by 'decay_factor'
    # Return the updated learning rate


# Test cases:
print("Initial learning rate:", learning_rate)
print("Decayed LR 1:", decay_learning_rate(0.9))  # Expected: 0.009
print("Decayed LR 2:", decay_learning_rate(0.5))  # Expected: 0.0045
print("Final global learning rate:", learning_rate) # Expected: 0.0045


# ==========================================
# Exercise 2: Stateful EMA Loss Tracker
# ==========================================

print("\n--- Exercise 2: Stateful EMA Loss Tracker ---")

def create_ema_tracker(beta):
    ema_loss = None
    # TODO: Define a variable 'ema_loss' initialized to None
    
    def track_loss(current_loss):
        # TODO: Declare 'ema_loss' as nonlocal
        nonlocal ema_loss
        if ema_loss is None:
            ema_loss = current_loss
        else:
            ema_loss = (beta * ema_loss) + (1 - beta) * current_loss
        return ema_loss
    return track_loss

        # If 'ema_loss' is None (first run), set it directly to 'current_loss'
        # Otherwise, calculate: (beta * old_ema) + (1 - beta) * current_loss
        # Return the updated 'ema_loss'

# Test tracking
tracker = create_ema_tracker(beta=0.9)
print("EMA Step 1 (Loss=1.5):", tracker(1.5))  # Expected: 1.5 (first run)
print("EMA Step 2 (Loss=1.0):", tracker(1.0))  # Expected: 0.9 * 1.5 + 0.1 * 1.0 = 1.45
print("EMA Step 3 (Loss=0.8):", tracker(0.8))  # Expected: 0.9 * 1.45 + 0.1 * 0.8 = 1.385


# ==========================================
# Exercise 3: Config Shadowing & LEGB Check
# ==========================================

print("\n--- Exercise 3: Config Shadowing ---")

model_name = "ResNet-50"

def train_model(epochs):
    # Local variable
    batch_size = 32
    
    def run_epoch():
        # TODO: Print: "Training [model_name] with batch size [batch_size]..."
        # Note: Both variables are resolved automatically via LEGB lookup order.
        print(f"Training {model_name} with batch size {batch_size}...")
        
    run_epoch()

# Test call:
train_model(5)


# ==========================================
# Answers to Socratic Questions
# ==========================================
# Write your answers below:
# 1- Difference between global and nonlocal:
# global is defined outside any function whereas nonlocal is used in nested functions
# 2- Variable shadowing and why it's dangerous:
# Variable shadowing means using variable within function with different value other than assigned outside the function.
# It is dangerous because it would create problems while debugging it from the code
