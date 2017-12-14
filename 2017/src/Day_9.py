
input_file = open("../inputs/Day_9.txt")


def remove_cancellations(l):
    new_list = []
    i = 0
    while i < len(l):
        if l[i] == '!':
            i += 1
        else:
            new_list.append(l[i])
        i += 1
    return new_list


def remove_garbage(l):
    new_list = []
    i=0
    garbage_count = 0
    while i < len(l):
        if l[i] == '<':
            i += 1
            while l[i] != '>':
                i += 1
                garbage_count += 1
        try:
            new_list.append(l[i])
        except IndexError:
            pass
        i += 1
    return [new_list, garbage_count]

stream = list(input_file.readline())


stream = remove_cancellations(stream)

stream, garbage_count = remove_garbage(stream)

score = 0
index = 0
while index < len(stream):
    if stream[index] == '{':
        group_count = 1
        group_score = 1
        index += 1
        while group_count > 0:
            if stream[index] == '{':
                group_score += group_count + 1
                group_count += 1
            if stream[index] == '}':
                group_count -= 1
            index += 1
    score += group_score
    index += 1


print(f"Score: {score}")
print(f"Garbage removed: {garbage_count}")