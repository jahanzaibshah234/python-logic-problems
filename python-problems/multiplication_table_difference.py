# Multiplication Table Differnce

# Ask for user input
n1 = int(input())
n2 = int(input())

# for-loop to iterate and print difference
for i in range(1, 11):
    n = n1 - n2
    print(n, "x", i, "=", n*i)
