"""Ask the user to enter a number n.
Print numbers from 1 to n, each on a new line."""

# Pseudocode
# Get number from user
# convert to interger
# Iterate on number
# print number from 1 to n each on new line

# Ask for user Input
n = input("Enter a number: ")

# Convert to interger
n = int(n)

# for loop to iterate on number from 1 to n
for i in range(1, n + 1):
    print(i)