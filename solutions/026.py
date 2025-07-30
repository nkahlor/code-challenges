def find_fraction_cycle_length(numerator: int, denominator: int) -> int:
    remainders_seen: dict[int, int] = {}
    has_cycle = False
    i = 0
    remainder = numerator

    if numerator < denominator:
        while remainder > 0:
            remainder *= 10
            if remainder in remainders_seen:
                has_cycle = True
                break
            remainders_seen.setdefault(remainder, i)
            digit = remainder // denominator
            remainder -= digit * denominator
            i += 1

    cycle_length = i - remainders_seen[remainder] if has_cycle else 0
    return cycle_length


def solve() -> int:
    longest_denominator = 2
    longest_cycle = 0
    for d in range(999, 2, -1):
        if d - 1 <= longest_cycle:
            break
        cycle_length = find_fraction_cycle_length(1, d)
        if cycle_length > 0:
            if cycle_length > longest_cycle:
                longest_cycle = cycle_length
                longest_denominator = d
    return longest_denominator


if __name__ == "__main__":
    print(solve())
