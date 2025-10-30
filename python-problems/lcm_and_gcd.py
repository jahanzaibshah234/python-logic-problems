"""Given two integers a and b,
You have to compute their LCM and GCD and
return an array containing their LCM and GCD."""

import math

def lcmAndGcd(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return [lcm, gcd]

print(lcmAndGcd(14, 8))
