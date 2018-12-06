import re

input_file = "../inputs/Day_7.txt"


#Read file
with open(input_file) as f:
    lines = f.readlines()

calculations = dict()
results = dict()

for line in lines:
	(operations, result) = line.split('->')
	calculations[result.strip()] = operations.strip().split(' ')

def calculate(wire):
	try:
		return int(wire)
	except ValueError:
		pass
	if wire not in results:
		operations = calculations[wire]

		if len(operations) == 1:
			res = calculate(operations[0])
		else:
			operation = operations[-2]
			if operation == 'AND':
				res = calculate(operations[0]) & calculate(operations[2])
			elif operation == 'OR':
				res = calculate(operations[0]) | calculate(operations[2])
			elif operation == 'NOT':
				res = ~calculate(operations[1]) & 0xffff
			elif operation == 'RSHIFT':
				res = calculate(operations[0]) >> calculate(operations[2])
			elif operation == 'LSHIFT':
				res = calculate(operations[0]) << calculate(operations[2])
		results[wire] = res
	return results[wire]

a = calculate("a")

print(f'Part 1: {a}')

results = dict()

results["b"] = a 

a = calculate("a")

print(f'Part 2: {a}')

