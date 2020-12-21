
def run_program(ops, noun, verb):
	index = 0
	ops[1] = noun
	ops[2] = verb
	while ops[index] != 99:
		ops[ops[index+3]] = perform_operation(ops[index], ops[ops[index+1]], ops[ops[index+2]])
		index+=4
	return ops[0]


def perform_operation(operation, input1, input2):
	if operation == 1: return input1 + input2
	if operation == 2: return input1 * input2
	print("ERROR ERROR")

ops = [int(i) for i in open("../inputs/Day_2.txt").read().split(",")]

print("Part 1:\n" + str(run_program(ops, 12, 2)))

for noun in range(100):
	for verb in range(100):
		if 19690720 == run_program([int(i) for i in open("../inputs/Day_2.txt").read().split(",")], noun, verb):
			print("Part 2:\n" + str(100*noun + verb))
