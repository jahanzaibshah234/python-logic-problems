"""Problem : Floyd's Triangle Pattern
Ask the user for a number n.
Print Floyd's Triangle up to n rows.
"""

# Pseudocode
# Get int(number) from user
# Initialize accumulator variable
# Nested for-loop to iterate on rows & columns
# for i in range(control rows):
#   for j in range(print number in rows)
#       print(number pattern)
#       increment accumulator
# print(for next line)

# Ask for user input
n = int(input("Enter a Number: "))

# Initialzie accumulator variable
count = 1

# Nested for-loop
for i in range(1, n+1): # iterate on rows
    for j in range(1, i+1): # iterate on columns
        print(count, end=" ")
        count += 1
    print()