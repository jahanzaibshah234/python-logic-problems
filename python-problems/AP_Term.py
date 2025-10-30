"""Given three integers a, d and n. Where a is the first term, d is the common difference of an A.P.  Calculate the nth term of A.P. 
The nth term is given by an = a + (n-1)d"""

def nthTerm(a, d, n):
        a_n = a + (n - 1) * d
        return a_n
print(nthTerm(5, 2, 5))
