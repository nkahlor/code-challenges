def generate_next_number(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (x * 3) + 1

longest_length = 0
longest_seed = 1
cache = {1: 1}
for i in range(2, 1000000):
    length = 0
    seed_number = i
    next_number = i
    while next_number > 1:
        if next_number in cache:
            length += cache[next_number]
            break
        length += 1
        next_number = generate_next_number(next_number)
    cache[seed_number] = length
    if length > longest_length:
        longest_length = length
        longest_seed = seed_number

print(longest_length)
print(longest_seed)
