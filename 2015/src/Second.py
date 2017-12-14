input_file = open("../inputs/Day_2.txt")

boxes = [box.replace("\n", "") for box in input_file.readlines()]

wrapping_paper_needed = 0

for box in boxes:
    l, w, h = [int(dim) for dim in box.split('x')]
    side_1 = l*w
    side_2 = l*h
    side_3 = w*h
    wrapping_paper_needed += 2*(side_1 + side_2 + side_3) + min([side_1, side_2, side_3])

print(wrapping_paper_needed)