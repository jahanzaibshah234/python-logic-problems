"""Ask the user to enter a number.
Count how many digits in that number are even (i.e., divisible by 2), and print the count."""

# Pseudocode
# Get number from user
# Convert to integer
# Convert Negative to Positive
# Initialize Counter Variable
# While-loop to count digits divisible by 2
# while n > 0:
#       Extract last by % 10
#       Check if digit is even (digit % 2 == 0)
#       if yes, increase counter
#       remove the last digit by // 10
# print the count

# Ask for user input
n = int(input("Enter a Number: "))

# Convert Negative to Positive
n = abs(n)

# Initialize Counter
count = 0

# While-loop to count digits divisible by 2
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count += 1
    n = n // 10
# Print digit divisible by 2
print(f"Digits divisible by 2: {count}")
