"""Print right triangle pattern
Write a Python program that prints an right triangle pattern using asterisks."""

# Pseudocode
# SET number of rows to print
# LOOP from total rows down to 1
# PRINT asterisks equal to current row number

# Step 1: Set pattern size
star_to_print = 5

# Step 2: Print pattern
for i in range(1, star_to_print + 1):
    print("*" * i)