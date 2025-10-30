"""Horizontal Star Pattern
Ask the user for a number n.
Print a horizontal line of * of length n."""

# Pseudocode
# Get number from user
# Convert to integer
# for loop for iteration
# Print * Horizontally

# Ask for user input
n = int(input("Enter a Number: "))

# for-loop to print * horizontally
for i in range(n):
    print("*", end="")