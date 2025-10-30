"""Problem: Find the Greatest Common Divisor (GCD)

Write a program that takes two numbers as input and finds their GCD (Greatest Common Divisor)."""


a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

while b != 0:
    a, b = b, a % b

print("GCD of Number:", a)