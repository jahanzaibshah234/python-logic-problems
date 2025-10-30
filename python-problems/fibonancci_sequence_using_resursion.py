"""Problem:

Write a program that generates the Fibonacci sequence up to n terms."""

# Pseudocode
# Get input from user
# Use Recursive Method
# Handle case if number less than or equal to 1 return number
# Use Fibonanci formula of nth term f(n-1) + f(n-2)
# Print(nth fibonancci sequence)

# Ask for user input
n = int(input("Enter aNumber: "))

# Define a function with Recursive Method
def fibonancci_sequence(n):

    if n <= 1:
        return n
    else:
        return fibonancci_sequence(n -1) + fibonancci_sequence(n - 2)
  
print("Fibonacci sequence:")
for i in range(n):
    print(fibonancci_sequence(i), end=" ")
    

