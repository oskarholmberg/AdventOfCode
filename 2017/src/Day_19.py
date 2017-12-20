input_file = open("../inputs/Day_19.txt")

matrix = []         # Matrix representation of the trail.
letter_count = 0    # Keeps track of how many letters should be found.


for line in input_file:
    row = list(line)
    row = row[:-1]
    for char in row:
        if char.isalpha():
            letter_count += 1
    matrix.append(row)


def next_pos(d, c1, c2):
    """
    Returns the coordinates corresponding to taking one step in direction d.
    :param d: int direction to step, 0 = up, 1 = right, 2 = down, 3 = left
    :param c1: int start y coordinate
    :param c2: int start x coordinate
    :return: (int, int) coordinates after taking a step in direction d
    """
    if d == 0:
        return c1-1, c2
    if d == 1:
        return c1, c2+1
    if d == 2:
        return c1+1, c2
    if d == 3:
        return c1, c2-1
    else:
        raise AttributeError("Invalid direction", d, "given! Has to be in [0, 1, 2, 3]")


def char(m, c1, c2):
    """
    Character generator, will return the next step along the line.
    :param m: list(list(str)) matrix modeling the trail.
    :param c1: int start y coordinate
    :param c2: int start x coordinate
    :return: str next char in the trail.
    """
    direction = 2
    old_dir = direction
    while True:
        next_y, next_x = next_pos(direction, c1, c2)    # get coordinates for next step in current direction
        try:                                            # try in case next step is out of bounds.
            next_char = m[next_y][next_x]                   # get next character in matrix
            if next_char != " ":                            # if it's not an empty string (i.e trail continues straight)
                c1, c2 = next_y, next_x                         # set current coordinates to next coordinates
                old_dir = direction                             # save current direction
                yield next_char                                 # return char at current coordinates
            else:                                           # if it was an empty string
                if old_dir == direction:                        # if I haven't turned before
                    direction += 1                                  # turn right
                    direction %= 4
                else:                                       # if I have turned before
                    direction += 2                              # turn left
                    direction %= 4
        except IndexError:                      # if next step was out of bounds turn same way as above
            if old_dir == direction:
                direction += 1
                direction %= 4
            else:
                direction += 2
                direction %= 4


collected_letters = []
characters = char(matrix, 0, len(matrix[0])-1)
step_count = 1                                      # Start at one to count the starting point.

while len(collected_letters) < letter_count:        # while there are still letters to be found
    character = next(characters)                        # get the next character
    if character.isalpha():                             # if it is a letter
        collected_letters.append(character)                 # save it
    step_count += 1                                     # increment steps taken


# Print results:
print("Day 19 part 1:", "".join(collected_letters))
print("Day 19 part 2:", step_count)
