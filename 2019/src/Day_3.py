from collections import defaultdict


def manhattan_distance(x0, y0, x1, y1):
	return abs(x0-x1)+abs(y0-y1)

def get_direction(char):
	if char == "U":
		return (0, 1)
	if char == "R":
		return (1, 0)
	if char == "D":
		return (0, -1)
	if char == "L":
		return (-1, 0)

def draw_wire(moves):
	grid = defaultdict(int)
	current_pos = (0,0)
	steps = 1
	for move in moves:
		dirr = get_direction(move[0])
		dist = int(move[1:])
		for i in range(1, dist+1):
			pos = (current_pos[0] + i*dirr[0], current_pos[1] + i*dirr[1])
			grid[pos] = steps
			steps += 1
		current_pos = pos
	return grid;

lines = [line for line in open("../inputs/Day_3.txt").read().split("\n")]

first_wire = draw_wire(lines[0].split(","))
second_wire = draw_wire(lines[1].split(","))

intersection = list(set(first_wire) & set(second_wire))

print("Part 1:" + str(min([manhattan_distance(0, 0, i[0], i[1]) for i in intersection])))
print("Part 2:" + str(min([first_wire[i]+second_wire[i] for i in intersection])))