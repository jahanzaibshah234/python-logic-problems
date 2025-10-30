"""A series with same common difference is known as arithmetic series.
The first term of series is 'a' and common difference is d.
The series looks like a, a + d, a + 2d, a + 3d, . . .
Find the sum of series upto nth term."""


def sum_of_ap(n, a, d):
    ap_sum = n * (2 * a + (n - 1) * d) // 2
    return ap_sum

print(sum_of_ap(5, 1, 3))
