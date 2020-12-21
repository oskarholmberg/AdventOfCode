def trees_hit_with_slope(vX,vY,t):
	x,y,trees_hit = 0,0,0
	while y < len(t):
		if t[y][x] == '#':
			trees_hit = trees_hit + 1
		x = (x + vX)%len(t[0])
		y = y + vY
	return trees_hit

terrain = open("../inputs/Day_3.txt").read().split("\n")

print('Part 1:\n' + str(trees_hit_with_slope(3,1,terrain)))
print('Part 2:\n' + str(trees_hit_with_slope(1,1,terrain)
	*trees_hit_with_slope(3,1,terrain)
	*trees_hit_with_slope(5,1,terrain)
	*trees_hit_with_slope(7,1,terrain)
	*trees_hit_with_slope(1,2,terrain)))