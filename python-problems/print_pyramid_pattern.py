"""Print a pyramid pattern
Write a Python program that prints a centered pyramid pattern using asterisks."""

# Pseudocode
# SET number of rows for the pyramid
# FOR each row from 1 to total rows
# CALCULATE number of spaces needed
# CALCULATE number of stars needed
# PRINT spaces followed by stars

# Set pyramid size
star_to_print = 5

# Print pyramid pattern
for i in range(1, star_to_print + 1):
    spaces = star_to_print - i          # Calculate leading spaces
    stars = 2 * i - 1                   # Calculate number of stars
    print(" " * spaces + "*" * stars)   # Print the pattern line