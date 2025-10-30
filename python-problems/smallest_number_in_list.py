"""Problem: Find the Smallest Number in a List

Write a program that takes a list of numbers and finds the smallest element."""

arr = [1, 2, 3, 4, 5, -2]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest Number:", smallest)



