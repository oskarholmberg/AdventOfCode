import re

passwords = open("../inputs/Day_2.txt").read().split("\n")

count1 = 0
count2 = 0

for password in passwords:
	(d1, d2) = [int(c) for c in re.findall(r'(\d+)-(\d+)', password)[0]]
	l = re.findall(r'(\w+):', password)[0]
	p = re.sub(r'\d+-\d+ \w: ', '', password)
	if p.count(l) >= d1 and p.count(l) <= d2:
		count1 = count1 + 1
	if bool(p[d1-1] == l) ^ bool(p[d2-1] == l):
		count2 = count2 + 1

print("Part 1:\n" + str(count1))
print("Part 2:\n" + str(count2))