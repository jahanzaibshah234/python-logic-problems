"""Problem — Palindrome Check
Task:
Ask the user to enter a word or number. 
Check if it is a palindrome (the same forward and backward). 
Print "Palindrome" or "Not a Palindrome"."""

# Pseudocode
# Get input from user
# Lower string for case sensitive 
# Use Slicing to check if it is a palindrome
# Print "Palindrome" or "Not a Palindrome"

# Ask for user input
s = input("Enter a Word: ")

# Lower string for case sensitive
s = s.lower()

# Use Slicing to check Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")