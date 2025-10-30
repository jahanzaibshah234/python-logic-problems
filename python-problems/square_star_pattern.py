"""Square Star Pattern
Ask the user for a number n.
Print a square pattern of stars with n rows and n columns."""

# Pseudocode
# Get number from user
# Convert to integer
# for i in range(n): # to iterate on rows
#       for j in range(n):  # to iterate on columns
# print square star pattern

# Ask for user input
n = int(input("Enter a number: "))

# Nested for-loop to iterate on rows & columns
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()