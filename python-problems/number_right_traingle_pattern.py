"""Problem: Number right angle triangle Pattern
Ask the user for a number n.
Print a right angle triangle pattern where each row displays numbers from 1 to row number.
"""

# Pseudocode
# Get int(number) from user
# Nested for-loop to iterate on rows & columns
# for i in range(1, n+1):
#   for j in range(1, i+1)
#       print(number pattern)
# print(for next line)

# Ask for user input
n = int(input("Enter a Number: "))

# Nested for-loop to print number 
for i in range(1, n+1): # iterate on rows
    for j in range(1, i+1): # iterate on columns
        print(j, end="")
    print()