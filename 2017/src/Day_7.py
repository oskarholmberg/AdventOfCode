input_file = open("../inputs/Day_7.txt")


def calc_weight(parent):
    tot = 0
    if len(parent.children) == 0:
        return parent.weight
    for child in parent.children:
        tot += calc_weight(child)
    return tot + parent.weight


class Program(object):
    def __init__(self, _name, _weight, _children, _parent=None):
        self.name = _name
        self.weight = _weight
        self.children = _children
        self.parent = _parent
        self.child_weights = 0
        self.total_weight = 0

    def print(self):
        print(self.name, self.weight, self.child_weights, self.total_weight)

    def print_children(self):
        for child in self.children:
            child.print()

programs = []

for line in input_file:
    words = line.split()
    name = words[0]
    weight = int(words[1].replace("(", "").replace(")", ""))
    children = []
    if len(line.split("->")) > 1:
        children = [child.replace(",", "") for child in line.split("->")[1].split()]

    programs.append(Program(_name=name, _weight=weight, _children=children))

for program in programs:
    child_list = []
    for child in program.children:
        p_child = [c for c in programs if c.name == child][0]
        p_child.parent = program
        child_list.append(p_child)
    program.children = child_list

for program in programs:
    program.total_weight = calc_weight(program)

for program in programs:
    program.child_weights = program.total_weight-program.weight


def is_balanced(program):
    for i in range(1, len(program.children)):
        if program.children[i-1].total_weight != program.children[i].total_weight:
            return False
    return True


root_program = None
for program in programs:
    if not program.parent:
        root_program = program
        print("Part 1: ", program.name)

program_queue = [root_program]
while len(program_queue) > 0:
    next_program = program_queue.pop(0)
    for child in next_program.children:
        if not is_balanced(child):
            program_queue.append(child)

suspects = next_program.children
culprit = None
for i in range(len(suspects)):
    next = (i+1) % len(suspects)
    second = (i+2) % len(suspects)
    if suspects[i].total_weight != suspects[next].total_weight and suspects[i].total_weight != suspects[second].total_weight:
        culprit = suspects[i]
        print("Part 2: The culprit was", culprit.name, "and it weight was", culprit.weight, "instead of", culprit.weight - (culprit.total_weight - suspects[next].total_weight))