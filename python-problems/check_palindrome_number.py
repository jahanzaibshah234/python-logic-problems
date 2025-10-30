"""Problem: Check for Palindrome Number

Write a program that takes an integer as input and checks if it is a palindrome.
(A palindrome number reads the same backward as forward, e.g., 121, 1331)."""

n = int(input("Enter a Number: "))

n = abs(n)

temp = n

res = 0

while n > 0:
    digit = n % 10
    res = (res * 10) + digit
    n = n // 10

if temp == res:
    print("Palindorme")
else:
   print("Not a Palindrome")