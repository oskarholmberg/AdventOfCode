import re

input_file = "../inputs/Day_3.txt"

#Read file
with open(input_file) as f:
    lines = f.readlines()

fabric = [[list() for col in range(1000)] for row in range(1000)]

claims = list()

for line in lines:
	claim_id = re.findall(r'#(\d+)', line)[0]
	claims.append(claim_id)
	(s, e) = [int(c) for c in re.findall(r'(\d+),(\d+)', line)[0]]
	(w, h) = [int(c) for c in re.findall(r'(\d+)x(\d+)', line)[0]]
	for x in range(s, s+w):
		for y in range(e, e+h):
			fabric[x][y].append(f'{claim_id}')
			if len(fabric[x][y]) > 1:
				claims = [claim for claim in claims if claim not in fabric[x][y]]
overlaps = 0

for col in range(1000):
	for row in range(1000):
		if len(fabric[col][row]) > 1:
			overlaps += 1

print(f'Part 1: {overlaps}')

print(f'Part 2: {claims[0]}')

