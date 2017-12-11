input_file = open("../inputs/first.txt")

stream = list(input_file.readline())
floor = 0

for c in stream:
    if c == '(': floor += 1
    elif c == ')': floor -= 1
print(floor)