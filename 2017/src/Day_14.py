from PIL import Image
import random


from Day_10 import knot_hash

input_file = open("../inputs/Day_14.txt")

key = input_file.readline()
hashes = []

for i in range(128):
    key_string = key + "-" + str(i)
    h = knot_hash(key_string)
    b = [bin(int(c, 16))[2:].zfill(4) for c in h]
    b = "".join(b)
    hashes.append([int(c) for c in list(b)])

img_array = []
for i in range(len(hashes)):
    for j in range(len(hashes[0])):
        if hashes[i][j] == 1:
            img_array.append((255, 255, 255))
        else:
            img_array.append((0, 0, 0))


def get_squares():
    return sum(map(sum, hashes))


print("Part 1:", get_squares())


def remove_group(x, y, color):
    n_locs = [(x, max(0, y - 1)), (min(x + 1, len(hashes) - 1), y), (x, min(y + 1, len(hashes) - 1)), (max(x - 1, 0), y)]
    hashes[x][y] = 0
    img_array[x*len(hashes)+y] = color
    for loc in n_locs:
        if hashes[loc[0]][loc[1]] == 1:
            remove_group(loc[0], loc[1], color)


def to_pdf(count):
    img = Image.new('RGB', (128, 128))
    img.putdata(img_array)
    img.save(f'../images/image-{count}.png')


region_count = 0
to_pdf(region_count)
for i in range(len(hashes)):
    for j in range(len(hashes[0])):
        if hashes[i][j] == 1:
            remove_group(i, j, (random.randrange(256), random.randrange(256), random.randrange(256)))
            to_pdf(region_count)
            region_count += 1

print("Part 2:", region_count)
