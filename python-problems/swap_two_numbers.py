"""Swap two numbers without temporary variable
Write a Python program that swaps the values of two variables without using a temporary variable."""

# Pseudocode
# INITIALIZE two variables with values
# SWAP values using arithmetic operations
# PRINT swapped values

# Step 1: Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"\nBefore swapping: a = {a}, b = {b}")

# Step 2: Swap values
a = a + b
b = a - b
a = a - b

# Step 3: Print results
print("After swapping:")
print("a =", a)
print("b =", b)