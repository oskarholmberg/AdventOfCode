input_file = open("../inputs/seventh.txt")

parents = []
children = []

for line in input_file:
    words = line.split()
    name = words[0]
    if len(line.split("->")) > 1:
        for child in line.split("->")[1].split():
            children.append(child.replace(",", ""))
    parents.append(name)

for parent in parents:
    if parent not in children:
        print(parent)
        break
