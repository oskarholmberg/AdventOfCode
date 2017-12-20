input_file = open("../inputs/Day_2.txt")

boxes = [box.replace("\n", "") for box in input_file.readlines()]

wrapping_paper_needed = 0
ribbon_needed = 0

for box in boxes:
    h, w, l = sorted([int(dim) for dim in box.split('x')])
    side_1 = l*w
    side_2 = l*h
    side_3 = w*h
    wrapping_paper_needed += 2*(side_1 + side_2 + side_3) + min([side_1, side_2, side_3])
    ribbon_needed += 2*h + 2*w + h*w*l

print("Day 2 part 1:", wrapping_paper_needed)
print("Day 2 part 2:", ribbon_needed)