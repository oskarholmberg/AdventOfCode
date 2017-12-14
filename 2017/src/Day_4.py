input_file = open("../inputs/Day_4.txt", 'r')

invalid_phrases_p1 = 0
invalid_phrases_p2 = 0
lines = 0


def is_anagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return str1_list == str2_list


for line in input_file:
    lines += 1
    pass_phrase = line.split()
    for word in pass_phrase:
        if pass_phrase.count(word) > 1:
            invalid_phrases_p1 += 1
            break
    for i in range(len(pass_phrase)):
        old_invalid = invalid_phrases_p2
        for j in range(len(pass_phrase)):
            if i != j and is_anagram(pass_phrase[i], pass_phrase[j]):
                invalid_phrases_p2 += 1
                break
        if old_invalid != invalid_phrases_p2:
            break

print("Part 1: ", lines - invalid_phrases_p1)
print("Part 1: ", lines - invalid_phrases_p2)