input_file = open("../inputs/fourth.txt", 'r')

invalid_phrases = 0
lines = 0

for line in input_file:
    lines += 1
    pass_phrase = line.split()
    for word in pass_phrase:
        if pass_phrase.count(word) > 1:
            invalid_phrases += 1
            break

print(lines - invalid_phrases)