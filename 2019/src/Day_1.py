def add_fuel_for_fuel(weight):
	weight = weight/3-2
	if weight <= 0: return 0
	return weight + add_fuel_for_fuel(weight)

fuel_for_modules = [int(i)/3-2 for i in open("../inputs/Day_1.txt").read().split("\n")]

print("Part 1:\n" + str(sum(fuel_for_modules)))

print("Part 2:\n" + str(sum([i+add_fuel_for_fuel(i) for i in fuel_for_modules])))

