import re

input_file = "../inputs/Day_6.txt"

#Read file
with open(input_file) as f:
    lines = f.readlines()


def toggle(grid, start, end, toggle):
	for x in range(int(start[0]), int(end[0])+1):
		for y in range(int(start[1]), int(end[1])+1):
			if toggle == "on":
				grid[x][y] = 1
			elif toggle == "off":
				grid[x][y] = 0
			else:
				grid[x][y] = (grid[x][y] + 1)%2

def increment(grid, start, end, toggle):
	for x in range(int(start[0]), int(end[0])+1):
		for y in range(int(start[1]), int(end[1])+1):
			if toggle == "on":
				grid[x][y] += 1
			elif toggle == "off" and grid[x][y] > 0:
				grid[x][y] -= 1
			elif toggle == "toggle":
				grid[x][y] += 2


gridP1 = [[0 for col in range(1000)] for row in range(1000)]
gridP2 = [[0 for col in range(1000)] for row in range(1000)]

switches = {}
switches["on"] = list()
switches["off"] = list()
switches["toggle"] = list()

for line in lines:
	start = re.findall(r"(\d+,\d+)", line)[0]
	end = re.findall(r"(\d+,\d+)", line)[1]
	if len(re.findall(r"turn on", line)) > 0:
		toggle(gridP1, start.split(','), end.split(','), "on")
		increment(gridP2, start.split(','), end.split(','), "on")
	elif len(re.findall(r"turn off", line)) > 0:
		toggle(gridP1, start.split(','), end.split(','), "off")
		increment(gridP2, start.split(','), end.split(','), "off")
	else:
		toggle(gridP1, start.split(','), end.split(','), "toggle")
		increment(gridP2, start.split(','), end.split(','), "toggle")


print(f'Part 1: {sum([sum(i) for i in zip(*gridP1)])}')
print(f'Part 2: {sum([sum(i) for i in zip(*gridP2)])}')


