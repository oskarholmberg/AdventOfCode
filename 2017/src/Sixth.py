input_file = open("../inputs/sixth.txt")

banks = [int(line) for line in input_file.readline().split()]
keys = []
key = ""
runs = 0

while keys.count(key) < 2:
    index = banks.index(max(banks))
    blocks = banks[index]
    banks[index] = 0
    while blocks > 0:
        index = (index + 1) % len(banks)
        banks[index] += 1
        blocks -= 1
    key = str(banks)
    keys.append(key)
    runs += 1

print("Part 1: ", runs)

cycle_size = [i for i, j in enumerate(keys) if j == key]

print("Part 2: ", cycle_size[1]-cycle_size[0])