input_file = open("../inputs/Day_5.txt")

jump_instructions = []

for line in input_file:
    jump_instructions.append(int(line))

current_index = 0
next_index = 0
jumps = 0

while next_index < len(jump_instructions):
    next_index = current_index+jump_instructions[current_index]
    jump_instructions[current_index] += 1
    current_index = next_index
    jumps += 1

print("Part 1: ", jumps)

input_file = open("../inputs/Day_5.txt")

jump_instructions = []

for line in input_file:
    jump_instructions.append(int(line))

current_index = 0
next_index = 0
jumps = 0

while next_index < len(jump_instructions):
    next_index = current_index+jump_instructions[current_index]
    if jump_instructions[current_index] >= 3:
        jump_instructions[current_index] -= 1
    else:
        jump_instructions[current_index] += 1
    current_index = next_index
    jumps += 1

print("Part 2: ", jumps)