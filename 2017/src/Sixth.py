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
        index += 1
        if index >= len(banks):
            index = 0
        banks[index] += 1
        blocks -= 1
    key = str(banks)
    keys.append(key)
    runs += 1

print(runs)