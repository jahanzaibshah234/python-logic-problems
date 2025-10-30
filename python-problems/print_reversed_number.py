"""Ask the user to enter a number.
Reverse the digits and print the reversed number."""

# Pseudocode
# Get number from user
# Convert to integer
# Convert negative to positive
# Create accumulator Variable
# while-loop to reverse the digits
# print the reversed number

# Ask for user input
n = int(input("Enter a number: "))

# Convert negative to positive
n = abs(n)

# Create accumulator variable
reversed_num = 0

# while-loop to reverse digits
while n > 0:
    digit = n % 10
    reversed_num = (reversed_num * 10) + digit
    n = n // 10

# Print the reversed number
print(f"Reversed Number: {reversed_num}")