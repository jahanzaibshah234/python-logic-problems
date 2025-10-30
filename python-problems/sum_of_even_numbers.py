"""Ask the user to enter a number n.
Print the sum of even numbers only from 1 to n."""

# Pseudocode
# Get number from user
# convert to integer
# Initialize accumulator
# for-loop to iterate on number
# add even number to total to get sum of even number
# print sum of even numbers

# Ask for user input
n = input("Enter a number: ")

# Convert it to interger
n = int(n)

# Initialize accumulator
total = 0

# for loop to iterate on number from 1 to n
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
# print the final sum
print(total)