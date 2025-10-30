"""Ask the user to enter a number n.
Print numbers from 1 to n using a while loop."""

# Pseudocode
# Get number from user
# convert to integer
# Initialize counter variable
# while loop to count number from 1 to n
# print number 1 to n

# Ask for user input
n = input("Enter a Number: ")

# Convert to integer
n = int(n)

# Initialize counter
count = 1

# while to count number from 1 to n
while count <= n:
    print(count)
    count += 1