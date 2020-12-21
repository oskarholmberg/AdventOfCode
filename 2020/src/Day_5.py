def get_pos(sequence, i, f, t):
	if f == t:
		return f
	else:
		if sequence[i] in ['F','L']:
			return get_pos(sequence, i+1, f, t-((t-f)/2)-1)
		return get_pos(sequence, i+1, f+((t-f)/2)+1, t)

scans = open("../inputs/Day_5.txt").read().split("\n")

max_seat_id = 0
seat_ids = list()

for scan in scans:
	row = get_pos(scan[:-3], 0, 0, 127)
	col = get_pos(scan[7:], 0, 0, 7)
	seat_id = row * 8 + col
	seat_ids.append(seat_id)
	if seat_id > max_seat_id:
		max_seat_id = seat_id

for seat_id in seat_ids:
	if seat_id + 1 not in seat_ids:
		my_seat_id = seat_id + 1
		break

print('Part 1:\n' + str(max_seat_id))
print('Part 2:\n' + str(my_seat_id))