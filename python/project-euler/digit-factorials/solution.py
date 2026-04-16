"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

"""
Notes

Need at least 2 digits to generate a sum, therefore
lower bound: x >= 10

largest digit is 9!, so the largest sum will be an n digit integer of the following form:
n * 9!

for n = 7 => 7 * 9! = 2540160 which is 7 digits, the smallest 7 digit number is 1,000,000
for n = 8 => 8 * 9! = 2903040 which is 7 digits, but n is 8. The smallest 8 digit number is 10,000,000
The largest 8 digit factorial sum is smaller than the smallest 8 digit number

upper bound: 2540160 
"""


fact_map = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880,
}


overall_sum = 0
for x in range(10, 2540160):
    original_num = x
    digit_fact_sum = 0
    while x > 0:
        digit = x % 10
        digit_fact_sum += fact_map[digit]
        x = x // 10

    if original_num == digit_fact_sum:
        overall_sum += original_num

print(overall_sum)
