"""Problem: Diamond Star Pattern
Ask the user for a number n.
Print a diamond-shaped pattern with 2n-1 rows.
First n rows will form the top pyramid.
Next n-1 rows will form the inverted pyramid."""

# Pseudocode
# Get int(number) from user
# for i from 1 to n+1:
#       spaces = n - i
#       star = 2 * i -1
#       print(stars)
# for j from n-1 to 1
#       spaces = n - i
#       star = 2 * i -1
#       print(spaces and stars) 

# Ask for user input
n = int(input("Enter a Number: "))

# Top pyramid
for i in range(1, n+1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Bottom inverted pyramid
for j in range(n-1, 0, -1):
    space = n - j
    star = 2 * j - 1
    print(" " * space + "*" * star)
