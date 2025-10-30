"""Problem: Calculate the Average of a List
Task:
Write a program that takes a list of numbers and calculates their average (mean)."""

arr = [2, 3, 4, 5, 6]

if len(arr) > 0:
    average = sum(arr) / len(arr)
    print("Average:", average)
else:
    print("The List is empty, no average.")
