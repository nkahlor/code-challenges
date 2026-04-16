"""
The fraction 49/98 is a curious fraction. An inexperienced mathematician, may incorrectly believe that 49/98 = 4/8 is obtained by cancelling the 9s.

we shall consider fractions like 30/50 = 3 / 5 to be trivial examples

there are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

"""
1 > x > 0
x = a / b
"""

res = []
for numerator in range(10, 100):
    numerator_ones = numerator % 10
    numerator_tens = (numerator // 10) % 10
    if numerator_ones == 0 or numerator_tens == 0:
        continue
    for denominator in range(10, 100):
        denominator_ones = denominator % 10
        denominator_tens = (denominator // 10) % 10
        if denominator_ones == 0 or denominator_tens == 0:
            continue
        candidates = [
            # (numerator_digit_cancelled, denominator_digit_cancelled, remaining_num, remaining_denom)
            (numerator_ones, denominator_ones, numerator_tens, denominator_tens),
            (numerator_tens, denominator_tens, numerator_ones, denominator_ones),
            (numerator_ones, denominator_tens, numerator_tens, denominator_ones),
            (numerator_tens, denominator_ones, numerator_ones, denominator_tens),
        ]
        if numerator / denominator >= 1:
            continue
        for num_cancel, denom_cancel, num_remain, denom_remain in candidates:
            if num_cancel != denom_cancel:
                continue
            if denom_remain == 0:
                continue
            if num_remain / denom_remain == numerator / denominator:
                res.append((num_remain, denom_remain))
final_num = 1
final_denom = 1
for num, denom in res:
    final_num *= num
    final_denom *= denom

print(final_num)
print(final_denom)
