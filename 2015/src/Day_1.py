input_file = open("../inputs/Day_1.txt")

stream = list(input_file.readline())
floor = 0
index = None

for i in range(len(stream)):
    if stream[i] == '(': floor += 1
    elif stream[i] == ')': floor -= 1
    if not index and floor < 0:
        index = i

print("Day 1 part 1:", floor)
print("Day 1 part 2:", index+1)