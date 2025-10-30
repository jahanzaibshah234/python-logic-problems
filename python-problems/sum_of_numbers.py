"""Ask the user to enter a number n.
Print the sum of numbers from 1 to n.
Example:
If input is 5, output should be 15 (1+2+3+4+5)"""

# Pseudocode
# Get number from user
# convert to interger
# Initialize accumulator
# for-loop to Iterate on number
# add it total to get sum
# print sum of number from 1 to n 

# Ask for user Input
n = input("Enter a number: ")

# Convert to interger
n = int(n)

# Initialize accumulator
total = 0

# for loop to iterate on number from 1 to n
for i in range(1, n + 1):
    total += i
# Print the final sum
print(total)