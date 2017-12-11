import numpy as np

input_file = open("../inputs/third.txt")

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

