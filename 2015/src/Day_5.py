import re

input_file = "../inputs/Day_5.txt"

#Read file
with open(input_file) as f:
    lines = f.readlines()

def isNicePart1(string):
	has_three_vowels = len(re.findall(r"[aeiou]", string)) > 2
	has_two_in_a_row = len(re.findall(r"(\w)\1+", string)) > 0
	no_illegal_matches = len(re.findall(r"ab|cd|pq|xy", string)) == 0
	return has_three_vowels and has_two_in_a_row and no_illegal_matches

def isNicePart2(string):
	has_pairs = len(re.findall(r"(\w{2}).*?(\1)", string)) > 0
	has_repeat = len(re.findall(r"(\w)\w\1", string)) > 0
	return has_pairs and has_repeat


countPart1 = 0
countPart2 = 0
for line in lines:
	if isNicePart1(line.strip()):
		countPart1 += 1
	if isNicePart2(line.strip()):
		countPart2 += 1

print(f'Part 1: {countPart1}')
print(f'Part 2: {countPart2}')