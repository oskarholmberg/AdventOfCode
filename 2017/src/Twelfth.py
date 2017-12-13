input_file = open("../inputs/twelfth.txt")

pipes = [line.replace("\n", "") for line in input_file.readlines()]


def find_group_with(program):
    visited = []
    next_locations = [program]
    while len(next_locations) > 0:
        current_location = next_locations.pop()
        visited.append(current_location)
        string = pipes[current_location].split("<->")
        destinations = [int(s) for s in string[1].split(",")]
        for dest in destinations:
            if dest not in visited:
                next_locations.append(dest)
    return visited


print("Part 1: ", len(find_group_with(0)))

not_visited = list(range(0, len(pipes)))
group_count = 0

while len(not_visited) > 0:
    index = not_visited.pop(0)
    not_visited = [item for item in not_visited if item not in find_group_with(index)]
    group_count += 1

print("Part 2: ", group_count)