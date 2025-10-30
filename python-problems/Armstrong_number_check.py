"""You are given a 3-digit number n, Find whether it is an Armstrong number or not."""

def armstrongNumber (n):
        num = str(n)
        num_len = len(num)
        sum = 0
        for i in num:
            sum += int(i) ** num_len
        return True if sum == n else False

print(armstrongNumber(153))