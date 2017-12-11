import math

input_file = open("../inputs/eleventh.txt")

directions = list(input_file.readline())

x, y = 0, 0
max_steps = 0

for dir in directions:
    if dir == 'n':
        x += 1
    if dir == 'ne':
        x += 1
        y += 1
    if dir == 'e':
        y +=1
    if dir == 'se':
        x -= 1
        y += 1
    if dir == 's':
        x -= 1
    if dir == 'sw':
        x -= 1
        y -= 1
    if dir == 'w':
        y -= 1
    if dir == 'nw':
        x += 1
        y -= 1
    steps = max(abs(x), abs(y))
    if steps > max_steps:
        max_steps = steps

print(f"Steps to child: {steps}")
print(f"Max distance away: {max_steps}")
