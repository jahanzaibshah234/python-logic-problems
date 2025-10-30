"""
Ask the user to enter a number.
Print:

"Even Positive" if the number is even and positive

"Odd Positive" if odd and positive

"Negative Number" if less than zero

"Zero" if it's zero
"""

# Pseudocode
# Get Number from User
# Condition Checking
# Print(Even Positive/Odd Positive/Negative Number/ Zero)

# Ask for user Input
num = input("Enter a Number: ")

# Convert to interger
num = int(num)

# Use if-else to check conditions
if num > 0 and num % 2 == 0:
    print("Even Positive")
elif num > 0:
    print("Odd Positive")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
