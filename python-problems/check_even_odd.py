'''
Write a program that takes a number from the user and tell wheather it is even or odd
'''
#Pseudocode
#Get Number from User
#Convert number to interger
#Check Wheather a number is even or odd
#print(Even/Odd)


# Take input from user
num = input("Enter a Number: ")

# Convert to integer
num = int(num)

# Check if num is even or odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
