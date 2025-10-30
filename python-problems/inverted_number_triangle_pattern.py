"""Problem: inverted number right angle triangle Pattern
Ask the user for a number n.
Print a inverted right angle triangle pattern.
"""

# Pseudocode
# Get int(number) from user
# Nested for-loop to iterate on rows & columns
# for i in range(n, 0, -1):
#   for j in range(1, i+1)
#       print(number pattern)
# print(for next line)

# Ask for user input
n = int(input("Enter a Number: "))

# Nested for-loop to print number 
for i in range(n, 0, -1): # iterate on rows
    for j in range(1, i+1): # iterate on columns
        print(j, end="")
    print()