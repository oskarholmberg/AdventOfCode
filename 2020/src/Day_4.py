import re

def byr_valid(byr):
	return 1920 <= int(byr) <= 2002

def iyr_valid(iyr):
	return 2010 <= int(iyr) <= 2020

def eyr_valid(eyr):
	return 2020 <= int(eyr) <= 2030

def hgt_valid(hgt):
	if re.search(r'cm',hgt):
		return 150 <= int(hgt[:-2]) <= 193
	elif re.search(r'in',hgt):
		return 59 <= int(hgt[:-2]) <= 76
	else:
		return False

def hcl_valid(hcl):
	return re.search(r'#([0-9a-f]*)', hcl) and len(re.findall(r'#([0-9a-f]*)', hcl)[0]) == 6

def ecl_valid(ecl):
	return ecl in ['amb','blu','brn','gry','grn','hzl','oth']

def pid_valid(pid):
	return re.search(r'(^\d{9}$)', pid)

passport_data = open("../inputs/Day_4.txt").read().split("\n\n")

keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

has_fields = list()
all_fields_valid = list()

for data in passport_data:
	if all(key+':' in data for key in keys):
		has_fields.append(data)
		if all(eval(key+'_valid(\''+re.findall(r''+ key +':([^\s]*)', data)[0]+'\')') for key in keys):
			all_fields_valid.append(data)

print('Part 1:\n' + str(len(has_fields)))
print('Part 2:\n' + str(len(all_fields_valid)))