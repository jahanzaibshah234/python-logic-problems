"""Problem: Hollow Diamond Pattern
Input number n.
Print a Hollow Diamond Star Pattern.
Same shape as Diamond, but stars only on boundary.
Inside should be empty spaces."""

# Pseudocode
# Get int(number) from user
# for i from 1 to n+1:
#       spaces = n - i
#       if-else for hollow condition
#       if i == 1 (first row):
#       print spaces followed by single line
#       else (rows with 2 stars):
#       star = 2 * (i-1) -1
#       print(spaces followed by a star, hollow space and than star)
# for j from n-1 to 1:
#       spaces = n - i
#       if-else for hollow condition
#       if j == 1 (last row):
#       print spaces followed by single line
#       else (rows with 2 stars):
#       star = 2 * (j-1) -1
#       print(spaces followed by a star, hollow space and than star)


# Ask for user input
n = int(input("Enter a Number: "))

# Top pyramid
for i in range(1, n+1):
    spaces = n - i
    if i == 1:
        print(" " * spaces + "*")
    else:
        hollow_space = 2 * (i -1) - 1
        print(" " * spaces + "*" + " " * hollow_space + "*")

# Bottom inverted pyramid
for j in range(n-1, 0, -1):
    space = n - j
    if j == 1:
        print(" " * space + "*")
    else:
        hollow_space = 2 * (j -1)- 1
        print(" " * space + "*" + " " * hollow_space + "*")



