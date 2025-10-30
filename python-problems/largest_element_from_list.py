"""Problem:

Write a program that finds the largest element in a list of numbers."""

# Pseudocode
# Create a list of numbers
# Set first element to largest
# For loop to check and update the largest
# Print(largest)

res = [2, 10, 8, 6, 4]

largest = res[0]

for num in res:
    if num > largest:
        largest = num

print("Largest Number:", largest)