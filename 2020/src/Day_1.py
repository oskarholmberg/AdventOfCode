import itertools

expenses = [int(i) for i in open("../inputs/Day_1.txt").read().split("\n")]

for a, b in itertools.combinations(expenses, 2):
    if a+b == 2020:
    	print("Part 1:\n" + str(a*b))

for a, b, c in itertools.combinations(expenses, 3):
    if a+b+c == 2020:
    	print("Part 2:\n" + str(a*b*c))


