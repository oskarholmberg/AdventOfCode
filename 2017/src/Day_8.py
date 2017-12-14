
input_file = open("../inputs/Day_8.txt")

registers = {}
commands = []
max_val = 0

for line in input_file:
    words = line.split()
    register = words[0]
    command = words
    if command[1] == 'dec':
        command[1] = '-'
    else:
        command[1] = '+'
    registers[register] = 0
    commands.append(command)


for command in commands:
    if eval('int(registers[command[4]])' + command[5] + 'int(command[6])'):
        new_val = eval('registers[command[0]]' + command[1] + 'int(command[2])')
        registers[command[0]] = new_val
        if new_val > max_val:
            max_val = new_val

print("Part 1: ", max(registers.values()))
print("Part 2: ", max_val)