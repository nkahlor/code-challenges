"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from math import sqrt


def special_pythagorean_triplet(n):
    for b in range(n - 2, -1, -1):
        for a in range(b - 1, 0, -1):
            c = sqrt(a ** 2 + b ** 2)
            if c.is_integer() and a + b + c == n:
                return a * b * int(c)
    print("No Solution")
    return None


print(special_pythagorean_triplet(1000))
