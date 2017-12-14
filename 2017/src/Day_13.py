input_file = open("../inputs/Day_13.txt")

lines = input_file.readlines()

firewall = {}

index = 0

for line in lines:
    line = line.replace("\n", "").split(": ")
    firewall[int(line[0])] = int(line[1])


def severity(delay):
    _severity = 0
    for key, value in firewall.items():
        if (key+delay) % (2 * (value - 1)) == 0:
            penalty = max(1, key*value)
            _severity += penalty
    return _severity


print("Part 1: ", severity(0))

waited = 0
while severity(delay=waited) != 0:
    waited += 1

print("Part 2: ", waited)