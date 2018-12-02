import hashlib

input_file = "../inputs/Day_4.txt"

#Read file
with open(input_file) as f:
    key = f.readline()

def hash(match, slice):
	count = 0
	hash = hashlib.md5((key + str(count)).encode()).hexdigest()
	while hash[:slice] != match:
		count += 1
		hash = hashlib.md5((key + str(count)).encode()).hexdigest()

	return count

#Part 1
print(f'Part 1: {hash("00000", 5)}')

#Part 2
print(f'Part 2: {hash("000000", 6)}')




