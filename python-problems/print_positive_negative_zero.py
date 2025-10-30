"""
Write a Python program that asks the user to enter a number, and prints whether it's:
Positive
Negative
Or Zero

"""
# Pseudocode
# Get a number from user
# Convert to integer
# Conditional to check positive, negative, zero
# print "Positive/Negative/Zero"

# Ask for user inout
num = input("Enter a number: ")

# Convert to integer
num = int(num)

# Use if-else to check conditions
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")