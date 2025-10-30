"""Problem: Right-Aligned Triangle Pattern
Ask the user for a number n.
Print a right-aligned triangle of stars (*) with n rows."""

# Pseudocode
# Get int(number) from user
# for i from 1 to n+1:
#       spaces before stars
#       print(spaces and stars) 

# Ask for user input
n = int(input("Enter a Number: "))

# for-loop to print right-aligned triangle pattern
for i in range(1, n+1):
    spaces = n - i
    print(" " * spaces + "*" * i)