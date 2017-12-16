
class Day5(object):
    def __init__(self, path):
        self.path = path
        self.jump_instructions = [int(line) for line in open(self.path)]
        self.current_index = 0
        self.next_index = 0
        self.jumps = 0

    def solve(self):
        while self.next_index < len(self.jump_instructions):
            self.next_index = self.current_index+self.jump_instructions[self.current_index]
            self.jump_instructions[self.current_index] += 1
            self.current_index = self.next_index
            self.jumps += 1

        print("Day 5 part 1: ", self.jumps)

        self.jump_instructions = [int(line) for line in open(self.path)]
        self.current_index = 0
        self.next_index = 0
        self.jumps = 0

        while self.next_index < len(self.jump_instructions):
            self.next_index = self.current_index+self.jump_instructions[self.current_index]
            if self.jump_instructions[self.current_index] >= 3:
                self.jump_instructions[self.current_index] -= 1
            else:
                self.jump_instructions[self.current_index] += 1
            self.current_index = self.next_index
            self.jumps += 1

        print("Day 5 part 2: ", self.jumps)


day_5 = Day5("../inputs/Day_5.txt")
day_5.solve()

