"""Ask the user to enter a number.
Print how many digits are in that number."""

# Pseudocode
# Get number from user
# Convert to integer
# Convert negative to positive
# Initialize counter variable
# While to count digits in number
# print(number of digit)

# Ask for user input
n = int(input("Enter a number: "))

# Convert negative to positive 
n = abs(n)

# Special case for 0
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n = n // 10  # Remove last digit

# Print the result
print("Number of digits:", count)