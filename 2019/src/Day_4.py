import re

def increasing(number):
	return str(number) == "".join(sorted(str(number)))

def two_adjecent(number):
	regex = r"(\d)\1"
	return len(re.findall(regex, str(number))) > 0

def exactly_two_adjecent(number):	
	regex = r"(\d)\1+"
	return any(len(m.group(0)) == 2 for m in re.finditer(regex, str(number)))

pw_range = [int(i) for i in open("../inputs/Day_4.txt").read().split("-")]

pws_p1 = list()
pws_p2 = list()

for i in range(pw_range[0], pw_range[1]+1):
	if increasing(i) and two_adjecent(i):
		pws_p1.append(i)
		if exactly_two_adjecent(i):
			pws_p2.append(i)

print("Part 1:" + str(len(pws_p1)))
print("Part 2:" + str(len(pws_p2)))