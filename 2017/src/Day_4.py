
class Day4(object):

    def __init__(self, path):
        self.invalid_phrases_p1 = 0
        self.invalid_phrases_p2 = 0
        self.lines = 0
        self.input_file = open(path)

    @staticmethod
    def is_anagram(str1, str2):
        str1_list = list(str1)
        str1_list.sort()
        str2_list = list(str2)
        str2_list.sort()

        return str1_list == str2_list

    def solve(self):
        for line in self.input_file:
            self.lines += 1
            pass_phrase = line.split()
            for word in pass_phrase:
                if pass_phrase.count(word) > 1:
                    self.invalid_phrases_p1 += 1
                    break
            for i in range(len(pass_phrase)):
                old_invalid = self.invalid_phrases_p2
                for j in range(i+1, len(pass_phrase)):
                    if i != j and self.is_anagram(pass_phrase[i], pass_phrase[j]):
                        self.invalid_phrases_p2 += 1
                        break
                if old_invalid != self.invalid_phrases_p2:
                    break

        print("Day 4 part 1: ", self.lines - self.invalid_phrases_p1)
        print("Day 4 part 2: ", self.lines - self.invalid_phrases_p2)


day_4 = Day4("../inputs/Day_4.txt")
day_4.solve()
