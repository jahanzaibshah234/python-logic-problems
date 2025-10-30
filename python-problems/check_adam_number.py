"""Given a number N, write a program to check whether given number is Adam Number or not
returns the answer as "YES" if it is a Adam Number. Otherwise, returns "NO"..
Adam number is a number when reversed, the square of the number and the square of the
reversed number should be numbers which are reverse of each other."""

def checkAdamOrNot(N):
    def reversed_number(num):
        reversed_number = 0
        while num > 0:
            digit = num % 10
            reversed_number = (reversed_number * 10) + digit
            num = num // 10
        return reversed_number
    reversed_n = reversed_number(N)
    square_n = N ** 2
    sq_rev_n = reversed_n ** 2
    rev_sq_rev_n = reversed_number(sq_rev_n)
    if square_n == rev_sq_rev_n:
        return "YES"
    else:
        return "NO"
    
print(checkAdamOrNot(12))
        
        
            
            
