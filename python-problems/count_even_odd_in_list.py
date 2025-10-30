"""Problem: Count Even and Odd Numbers in a List

Write a program that takes a list of numbers and 
counts how many numbers are even and how many are odd."""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

for i in arr:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)
