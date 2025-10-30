"""Number of 1 Bits
Given a positive integer n. Your task is to return the count of set bits.
"""

def setBits(n):
    count = 0
    while n > 0:
        n = n&(n-1)
        count += 1
    
    return count

print(setBits(6))
