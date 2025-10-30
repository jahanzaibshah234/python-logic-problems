"""Problem: Pascal's Triangle (Half-Pyramid Version)
Ask the user for a number n.
Print a half Pascal's Triangle up to n rows using combination logic."""

# Pseudocode
# Get int(number) from user
# Nested for-loop to iterate on rows & columns
# for i from 0 to n-1:
#   for j from 0 to i:
#       print combination(i, j)
# print(new line)

# Import Library
import math

# Ask for user input
n = int(input("Enter a Number: "))

# Nested for-loop to print number 
for i in range(n): # iterate on rows (from 0 to n-1)
    for j in range(i + 1): # iterate on columns (from 0 to current row number i)
        print(math.comb(i, j), end=" ") # Print combination
    print() # New line