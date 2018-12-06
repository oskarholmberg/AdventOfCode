input_file = "../inputs/Day_2.txt"

#Read file
with open(input_file) as f:
    lines = f.readlines()

two_same_count = 0
three_same_count = 0

def diffPerChar(string1, string2):
	counter = 0
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			counter += 1
	return counter

def hasExactly(string, count):
	dictionary = dict.fromkeys(string, 0)
	for c in string:
		dictionary[c] += 1
	for v in dictionary.values():
		if v == count:
			return True
	return False

for line in lines:
	if hasExactly(line.strip(), 2):
		two_same_count += 1
	if hasExactly(line.strip(), 3):
		three_same_count += 1

print(f'Part 1: {two_same_count * three_same_count}')

for i in range(len(lines)):
	for k in range(i+1, len(lines)):
		if diffPerChar(lines[i].strip(), lines[k].strip()) == 1:
			result = ""
			for j in range(len(lines[i].strip())):
				if lines[i].strip()[j] == lines[k].strip()[j]:
					result += lines[i].strip()[j]

print(f'Part 2: {result}')