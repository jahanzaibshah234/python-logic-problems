"""Problem: You are given a number n.
Print the following number pyramid pattern"""

# Ask for user input
n = int(input("Enter a Number: "))

# Nested-loop to print number pyramid
for i in range(1, n + 1):
    spaces = n - i
    print(" " * spaces, end="")  # Print spaces first
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Newline after each row
