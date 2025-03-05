digits = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    70: 'seventy',
    60: 'sixty',
    80: 'eighty',
    90: 'ninety'
}

def number_to_string(x):
    # 0 -> 20 are in memory already
    if x >= 1 and x <= 20:
        return digits[x]
    # 21 -> 99 don't require the hundred modifier
    elif x >= 21 and x <= 99:
        remainder = x % 10
        tens = digits[x - remainder]
        ones = '' if remainder == 0 else digits[remainder]
        return tens + ones
    elif x >= 100 and x <= 999:
        remainder = x % 100
        hundreds =  digits[x // 100]
        ans = hundreds + 'hundred'
        if remainder > 0:
            ans += 'and' + number_to_string(remainder)
        return ans
    else:
        return 'onethousand'
    
    


ans = 0
n = 1000
for i in range(1, n + 1):
    current_number = number_to_string(i)
    print(current_number)
    ans += len(current_number)

print(ans)