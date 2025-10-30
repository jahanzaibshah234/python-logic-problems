"""Given a decimal number n, return its binary equivalent."""

def decToBinary(n):
# using built-in bin()
    #dec_to_bin = bin(n)
    #return dec_to_bin[2:]

    # manually using while-loop
    if n == 0:
        return "0"
    binary_num = ""
    while n > 0:
        remainder = n % 2
        binary_num = str(remainder) + binary_num
        n = n // 2
    return binary_num

print(decToBinary(12))

