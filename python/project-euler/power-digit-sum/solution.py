"""
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2 ** 1000?
"""

big_number = 2 ** 1000
digits = [int(digit) for digit in str(big_number)]
print(sum(digits))
