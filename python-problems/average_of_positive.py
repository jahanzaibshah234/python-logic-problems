"""Problem: Calculate the Average of Only Positive Numbers
Task:
Write a program that takes a list of numbers (which may include negative ones) 
and calculates the average of only the positive numbers.
If there are no positive numbers, print a message instead."""

arr = [2, 3, -4, 5, 6, -1, 7, -2]

pos_sum = 0
pos_count = 0

for num in arr:
    if num > 0:
        pos_sum += num
        pos_count += 1
        
if pos_count > 0:
    average = pos_sum / pos_count
    print("Average:", average)
else:
    print("The List is empty, no average.")

