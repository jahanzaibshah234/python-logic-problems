"""Problem: Prime Number

Write a program that asks the user for a number and checks whether it is prime or not."""

# Pseudocode
# Get input from user
# Initialize variable to track if it is prime
# Use a for-loop start from 2 to sqt of number
# If number is divisible by any value in the loop -> Not prime
# Else -> prime
# Print the result

n = int(input("Enter a Number: "))

def check_prime(n):
    if n <= 1:
        return f"{n} is Not a Prime Number"

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
           return f"{n} is Not a Prime Number"
    return f"{n} is a Prime Number"

print(check_prime(n))