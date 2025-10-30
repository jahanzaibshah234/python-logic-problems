"""Add two numbers
Write a Python program that asks the user to input two numbers and prints their sum."""

# Psuedocode
# GET first number from user
# GET second number from user
# ADD the numbers
# PRINT the result

# Step 1: Input from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Step 2: Convert to numbers
num1 = int(num1)
num2 = int(num2)

# Step 3: Add them
result = num1 + num2

# Step 4: Print the result
print("The sum is:", result)