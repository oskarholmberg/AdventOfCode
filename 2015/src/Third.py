import numpy as np

input_file = open("../inputs/third.txt")

directions = list(input_file.readline())

map = np.zeros((len(directions), len(directions)))
coordinates = [int(len(directions) / 2) - 1, int(len(directions) / 2) - 1]
map[coordinates[0], coordinates[1]] = 1

for dir in directions:
    if dir == '>':
        coordinates[1] += 1
    if dir == '<':
        coordinates[1] -= 1
    if dir == '^':
        coordinates[0] -= 1
    if dir == 'v':
        coordinates[0] += 1
    map[coordinates[0], coordinates[1]] += 1

print(len(map.nonzero()[0]))