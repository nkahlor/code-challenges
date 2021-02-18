# This is a pretty simple one, not much to talk about here

def get_multiples_of_3_and_5(n):
    return list(
        filter(
            lambda x: x % 3 == 0 or x % 5 == 0,
            range(1, n)
        )
    )

n = int(input("> n: "))
print(f"Sum of multiples: {sum(get_multiples_of_3_and_5(n))}")
