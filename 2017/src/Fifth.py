input_file = open("../inputs/fifth.txt")

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

print(jumps)