"""Ask the user to enter a number n.
Print the factorial of that number.
(Factorial means: n * (n-1) * (n-2) * ... * 1"""

# Pseudocode
# Get number from user
# convert number to integer
# Initialize accumulator
# Take the Factorial of that number
# print the factorial

# Ask for user input
n = input("Enter a number: ")

# Convert number to interger
n = int(n)

# Initialize accumulator
fact = 1

# Take Factorial of number
for i in range(1, n + 1):
    fact *= i
# print the factorial of number
print(fact)