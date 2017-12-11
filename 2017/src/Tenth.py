from functools import reduce

def sparse_hash(_list, _lengths, skip_size=0, current_position=0, laps=1):
    lap_count = 0
    while lap_count < laps:
        for length in _lengths:
            length = int(length)
            if length > len(_list):
                continue
            to_reverse = _list[current_position:current_position + length]
            if len(to_reverse) < length:
                to_reverse.extend(_list[0:length - len(to_reverse)])
            _reversed = list(reversed(to_reverse))
            for i in range(len(_reversed)):
                list_index = (current_position + i) % len(_list)
                _list[list_index] = _reversed[i]
            current_position += length + skip_size
            current_position = current_position % len(_list)
            skip_size += 1
        lap_count += 1
    return _list


input_string = open("../inputs/tenth.txt").readline()
lengths = input_string.split(",")

_hash = sparse_hash(_list=list(range(0, 256)), _lengths=lengths)

print(f"Part 1: {_hash[0]*_hash[1]}")

ascii_lengths = [ord(c) for c in list(input_string)]
ascii_lengths.extend([17, 31, 73, 47, 23])

sparse_hash = sparse_hash(_list=list(range(0, 256)), _lengths=ascii_lengths, laps=64)

dense_hash = []
for i in range(0, len(sparse_hash), 16):
    dense_hash.append(reduce(lambda i, j: int(i) ^ int(j), sparse_hash[i:i+16]))
dense_hash = ["{0:0{1}x}".format(i,2) for i in dense_hash]
print("".join(dense_hash))