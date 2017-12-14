

input_file = open("../inputs/Day_2.txt", 'r')

total_p1 = 0
total_p2 = 0


for line in input_file:
    values = [int(value) for value in line.split()]
    total_p1 += max(values) - min(values)
    for i in range(len(values)):
        val = list(filter(lambda x: x % values[i] == 0 and x != values[i], values))
        if len(val) != 0:
            total_p2 += int(val[0]/values[i])


print(f"Part 1: {total_p1}")

print(f"Part 2: {total_p2}")
