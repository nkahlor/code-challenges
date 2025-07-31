def solve() -> int:
    n = 101
    seen: set[int] = set()
    for a in range(2, n):
        y = a
        for _ in range(2, n):
            y *= a
            seen.add(y)
    return len(seen)


if __name__ == "__main__":
    print(solve())
