import csv


def get_char_value(c: str) -> int:
    return ord(c.upper()) - ord("A") + 1


names = []
with open("./data/0022_names.txt", "r", newline="", encoding="utf-8") as name_file:
    reader = csv.reader(name_file, delimiter=",", quotechar='"')
    names = list(reader)[0]

total = 0
sorted_names = sorted(names)
for i, name in enumerate(sorted_names):
    char_sum = sum([get_char_value(c) for c in name])
    total += char_sum * (i + 1)

print(total)
