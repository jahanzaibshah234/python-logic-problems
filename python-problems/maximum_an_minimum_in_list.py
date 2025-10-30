"""Problem: Find the Maximum and Minimum in a List
Task:
Write a program that takes a list of numbers and finds the largest and smallest number in it."""

arr = [3, 7, 2, 9, 5]

largest = arr[0]

smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print("Maximum:", largest)
print("Minimum:", smallest)