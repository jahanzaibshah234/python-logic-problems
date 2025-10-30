"""Problem: Count Prime Digits
Task:
Ask the user to enter an integer n.
Count how many prime digits (2, 3, 5, 7) are present in the number and print the count."""

# Pseudocode
# Get input from user
# Initialize counter
# Create a set of prime digits as strings
# Check each in the number
# for digit in number:
#   if digit in set(2, 3, 5, 7):
#       count += 1
# print(count)

# Ask for user input
n = input("Enter a Number: ")

# Initialize counter variable
count = 0

# Set of prime digits as strings
prime_number = {'2', '3', '5', '7'}

# Check each digit in the number
for digit in n:
    if digit in prime_number:
        count += 1
print("Count of prime digits:", count)


