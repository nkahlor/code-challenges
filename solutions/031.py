denominations = [1, 2, 5, 10, 20, 50, 100, 200]
paths: set[str] = set()

cache: dict[int, int] = {}


def dfs(target: int, path: list[str]) -> int:
    if target == 0:
        normalized_path = "->".join(sorted(path[:]))
        if normalized_path in paths:
            return 0

        return 1
    elif target < 0:
        return 0

    if target in cache:
        return cache[target]

    ways_to_split = 0
    for denomination in denominations:
        path.append(f"{denomination}")
        remaining = target - denomination
        ways_to_split += dfs(remaining, path)
        path.pop()
    cache[target] = ways_to_split
    return ways_to_split


def solve() -> int:
    target = 200
    val = dfs(target, [])
    # print(paths)
    # print(val)
    return len(paths)


if __name__ == "__main__":
    print(solve())
