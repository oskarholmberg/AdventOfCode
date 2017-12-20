input_file = open("../inputs/Day_3.txt")

directions = list(input_file.readline())

next_pos = (0, 0)

visited = [next_pos]


def get_new_pos(d, x, y):
    if d == '>':
        x += 1
    if d == '<':
        x -= 1
    if d == '^':
        y -= 1
    if d == 'v':
        y += 1
    return x, y


for direction in directions:
    next_pos = get_new_pos(direction, next_pos[0], next_pos[1])
    if next_pos not in visited:
        visited.append(next_pos)
print("Day 3 part 1:", len(visited))

santa_pos = (0, 0)
robo_pos = (0, 0)
visited = [santa_pos]

for i in range(len(directions)):
    if i % 2 == 0:
        santa_pos = get_new_pos(directions[i], santa_pos[0], santa_pos[1])
        if santa_pos not in visited:
            visited.append(santa_pos)
    else:
        robo_pos = get_new_pos(directions[i], robo_pos[0], robo_pos[1])
        if robo_pos not in visited:
            visited.append(robo_pos)

print("Day 3 part 2:", len(visited))


