"""Problem: Hollow Square Star Pattern
Ask the user for a number n.
Print a hollow square star pattern of size n x n."""

# Psuedocode
# Get number from user
# Nested for-loop to iterate on rows, columns
# for i in range(n):
#     for j in range(n):
#     if-else for conditions 
#      print(*)
# print()

# Ask user for input()
n = int(input("Enter a Number: "))
# Nested for-loop to iterate on rows & columns
for i in range(n): # iterate on rows
    for j in range(n): # iterate on columns
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

