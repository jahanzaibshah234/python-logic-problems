"""Ask the user to enter a number.
Print the total_sum of its digits using a while loop."""

# Pseudocode
# Get number from user
# Convert to Integer
# Convert Negative to Positive
# Initialize accumulator variable
# while-loop to calculate the total_sum of digits
# print total_sum of digits

# Ask for user input
n = int(input("Enter a number: "))

# Convert Negative to Positive
n = abs(n)

# Initialize accumulator
total_sum = 0

# while-loop to calculate digit sum
while n > 0:
    digit = n % 10
    total_sum += digit
    n = n // 10
# Print total_sum of digits
print(f"The Sum of Digits: {total_sum}")