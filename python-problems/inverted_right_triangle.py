"""Print inverted right triangle pattern
Write a Python program that prints an inverted right triangle pattern using asterisks."""

# Pseudocode
# SET number of rows to print
# LOOP from total rows down to 1
# PRINT asterisks equal to current row number
# END LOOP

# Set pattern size
star_to_print = 5

# Print pattern
for i in range(star_to_print, 0, -1):
    print("*" * i)