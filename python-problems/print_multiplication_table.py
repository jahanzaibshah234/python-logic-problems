"""Ask the user to enter a number n.
Print the multiplication table of n from 1 to 10."""

# Pseudocode
# Get number from user
# convert to integer
# Create accumulator variable
# for loop to iterate on number and assign it to accumulator variable
# print Multiplication table

# Ask for user input
n = input("Enter a number: ")

# Convert to integer
n = int(n)

# for-loop to iterate on number from 1 to n
for i in range(1, 11):
    table = n * i
# Print the multiplication table
    print(n, "x", i, "=", table)
