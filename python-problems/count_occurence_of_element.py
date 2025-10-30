"""Problem: Count Occurrences of an Element in a List

Write a program that takes a list and an element from the 
user and counts how many times that element occurs in the list"""

n = int(input("Enter a Number: "))

def checkElement(n):

    arr = [2, 3, 4, 5, 2, 6, 2]

    count = 0

    for i in arr:
        if i == n:
            count += 1
    return count

print(checkElement(n)) 