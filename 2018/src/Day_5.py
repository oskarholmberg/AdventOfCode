import re

lines = open('../inputs/Day_5.txt').read().split('\n')

polymers = 0

def react_polymers(line):
	done = False
	while not done:
		done = True
		pairs = re.findall(r'([a-z])([A-Z])', line)
		for pair in pairs:
			if pair[1] == pair[0].upper():
				line = line.replace(pair[0]+pair[1], '')
				done = False
		pairs = re.findall(r'([A-Z])([a-z])', line)
		for pair in pairs:
			if pair[1] == pair[0].lower():
				line = line.replace(pair[0]+pair[1], '')
				done = False
	return line

for line in lines:
	polymers += len(react_polymers(line))

print(f'Part 1: {polymers}')

smallest = 100000

for c in "abcdefghijklmnopqrstuvwxyz":
	for line in lines:
		line = line.replace(c, '')
		line = line.replace(c.upper(), '')
		temp = len(react_polymers(line))
		if temp < smallest:
			smallest = temp

print(f'Part 2: {smallest}')



