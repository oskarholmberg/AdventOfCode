import string

input_file = open("../inputs/Day_16.txt")

moves = input_file.readline().split(",")

programs = list(string.ascii_lowercase[0:16])


def perform_move(array, m):
    new_array = list(array)
    if m[0] == "s":
        spin = int(m[1:])
        last = array[-spin:]
        first = array[0:-spin]
        return last + first
    if m[0] == "x":
        index_1 = int(m.split("/")[0][1:])
        index_2 = int(m.split("/")[1])
        prog_1 = array[index_1]
        prog_2 = array[index_2]
        new_array[index_1] = prog_2
        new_array[index_2] = prog_1
        return new_array
    if m[0] == "p":
        prog_1 = m[1]
        prog_2 = m[3]
        index_1 = array.index(prog_1)
        index_2 = array.index(prog_2)
        new_array[index_1] = prog_2
        new_array[index_2] = prog_1
        return new_array
    else:
        raise AttributeError("Detected move of incorrect format.")


def dance_cycle(p, cycles):
    key = "".join(p)
    keys = [key]
    count = 0
    while keys.count(key) < 2 and count < cycles:
        for move in moves:
            p = perform_move(p, move)
        key = "".join(p)
        keys.append(key)
        count += 1
    if count != cycles:
        keys = keys[0:-1]
    index = cycles % len(keys)
    return keys[index]


print("Day 16 part 1:", "".join(dance_cycle(programs, 1)))
print("Day 16 part 2:", "".join(dance_cycle(programs, 1000000000)))
