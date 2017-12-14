import numpy as np

input_file = open("../inputs/Day_3.txt")

target = int(input_file.readline())

# To determine Manhattan Distance we need two numbers.
# Which layer target is in, and the distance from targets position to the center of that side.

counter = 1
side = 1
current_layer = [1]
layer_count = 0

while counter < target:
    # Add a layer
    layer_count += 1
    side += 2                    # New layer side length
    layer_pos = 0                # Position count of new layer
    current_layer = []           # Initialize vector of elements for new layer
    while layer_pos < side*4-4:  # While position count for layer is less than layer length, keep adding numbers to layer.
        counter += 1
        layer_pos += 1
        current_layer.append(counter)

# Split layer into sides
sides = [current_layer[i:i + side - 1] for i in range(0, len(current_layer), side - 1)]

# Find which side holds the target
for s in sides:
    if target in s:
        # Find which index on that side target is on. (Adding 1 since indices start at 0)
        index = s.index(target) + 1
        print(f"Part 1: {round(abs(index-side/2))+layer_count}")     # Add distances together and print


def sum_neighbours(m, i, j):
    region = m[max(0, i-1): i+2,
                    max(0, j-1): j+2]
    return np.sum(region) - m[i, j]


matrix = np.zeros((side, side))
coordinates = [int(side/2), int(side/2)]
matrix[coordinates[0]][coordinates[1]] = 1
side = 1
counter = 1

while counter < target:
    side += 2
    layer_pos = 1
    coordinates[1] += 1
    digits_in_layer = side*4-4
    while layer_pos <= digits_in_layer:
        counter = sum_neighbours(matrix, coordinates[0], coordinates[1])
        if counter > target:
            print(int(counter))
            break
        matrix[coordinates[0]][coordinates[1]] = counter
        if layer_pos/digits_in_layer < 0.25:
            coordinates[0] -= 1
        elif layer_pos/digits_in_layer < 0.5:
            coordinates[1] -= 1
        elif layer_pos/digits_in_layer < 0.75:
            coordinates[0] += 1
        elif layer_pos/digits_in_layer < 1:
            coordinates[1] += 1
        layer_pos += 1
