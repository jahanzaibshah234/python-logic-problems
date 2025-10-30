"""Print a simple star pattern
Ask the user for a number n.
Print a vertical line of * of length n"""

# Psuedocode
# Get number from user
# Convert to integer
# Initialize Counter Variable
# While count < n:
#     Print * each on new line

# Ask for user input
n = int(input("Enter a Number: "))

# Initialize Counter
count = 0

# While-loop to print * pattern
while count < n:
    print("*")
    count += 1
