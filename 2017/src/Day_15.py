import progressbar as pbar


def generator(value, factor, multiple_of=1):
    while True:
        value = value * factor % 2147483647
        while value % multiple_of != 0:
            value = value * factor % 2147483647
        yield value


bar = pbar.ProgressBar()

a_1 = generator(591, 16807)
b_1 = generator(393, 48271)

a_2 = generator(591, 16807, multiple_of=4)
b_2 = generator(393, 48271, multiple_of=8)

count_1 = 0
count_2 = 0
for i in bar(range(40000000)):
    if next(a_1) & 0xffff == next(b_1) & 0xffff:
        count_1 += 1
    if i % 8 == 0:
        if next(a_2) & 0xffff == next(b_2) & 0xffff:
            count_2 += 1

print("Day 15 part 1:", count_1)
print("Day 15 part 2:", count_2)



