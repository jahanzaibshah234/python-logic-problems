'''Write a Python program that asks the user to enter their name and age, then prints:
"Hello [name], you will be [age+1] years old next year."
'''
# Pseudocode
# Get name as input from user
# Get age as input from user
# Convert name to string and age to integer
# Print the formatted String

# Take input from user

name  = input("Enter your name: ")
age = input("Enter your age: ")

# Convert to str and int
name = str(name)
age = int(age)

# Print the Formatted String
print(f"Hello {name}, you will be {age + 1} years old next year.")
