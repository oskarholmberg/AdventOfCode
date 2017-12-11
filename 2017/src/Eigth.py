
input_file = open("../inputs/eigth.txt")

registers = {}
commands = []

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
        registers[command[0]] = eval('registers[command[0]]' + command[1] + 'int(command[2])')

print(max(registers.values()))
