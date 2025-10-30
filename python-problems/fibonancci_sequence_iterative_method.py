"""Problem:

Write a program that generates the Fibonacci sequence up to n terms."""

# Pseudocode
# Get input from user
# Use Iterative Method
# Create a list
# Use For-loop to iterate on n
# Append element to list
# Use formula a, b = b, a + b
# Print(nth fibonancci sequence)

# Ask for user input
n = int(input("Enter aNumber: "))

# Iterative Method
def fibonancci_sequence(n):

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence 

print("Fibonancci Sequence:")    
print(fibonancci_sequence(n))