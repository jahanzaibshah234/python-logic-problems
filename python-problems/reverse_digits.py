"""Problem: Reverse Digits
Task:
Ask the user to enter an integer n. Reverse the digits of the number and print the reversed number."""

# Pseudocode
# Get input from user
# Reversed string using slicing
# print reversed number

# Ask for user input
n = input("Enter a Number")

# Reverse string using slicing
reversed_number = int(n[::-1])

# Print reversed digits
print("Reversed Number: ", reversed_number)