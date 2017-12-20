from collections import defaultdict
import string


input_file=open("../inputs/Day_18.txt", 'r')
instr = [line.split() for line in input_file.read().strip().split("\n")]
input_file.close()

d1 = defaultdict(int) # registers for the programs
d2 = defaultdict(int)
d2['p'] = 1
ds = [d1, d2]


def to_int(s):
    if s in string.ascii_lowercase:
        return d[s]
    return int(s)


total_sent = 0

indices = [0, 0]       # instruction indices for both programs
queues = [[], []]           # queues of sent data (snd[0] = data that program 0 has sent)
states = ["ok", "ok"]        # "ok", "r" for receiving, or "done"
current_program = 0
d = ds[current_program]     # current program's registers
i = indices[0]         # current program's instruction index
while True:
    if instr[i][0] == "snd":    # send
        if current_program == 1: # count how many times program 1 sends
            total_sent += 1
        queues[current_program].append(to_int(instr[i][1]))
    elif instr[i][0]=="set":
        d[instr[i][1]] = to_int(instr[i][2])
    elif instr[i][0]=="add":
        d[instr[i][1]] += to_int(instr[i][2])
    elif instr[i][0]=="mul":
        d[instr[i][1]] *= to_int(instr[i][2])
    elif instr[i][0]=="mod":
        d[instr[i][1]] %= to_int(instr[i][2])
    elif instr[i][0]=="rcv":
        if queues[1-current_program]: # other program has sent data
            states[current_program] = "ok"
            d[instr[i][1]] = queues[1 - current_program].pop(0) # get data
        else: # wait: switch to other prog
            if states[1-current_program]== "done":
                break # will never recv: deadlock
            if len(queues[current_program]) == 0 and states[1-current_program] == "r":
                break # this one hasn't sent anything, other is receiving: deadlock
            indices[current_program] = i   # save instruction index
            states[current_program]= "r" # save state
            current_program = 1 - current_program   # change program
            i = indices[current_program] - 1 # (will be incremented back)
            d = ds[current_program]    # change registers
    elif instr[i][0] == "jgz":
        if to_int(instr[i][1]) > 0:
            i += to_int(instr[i][2]) - 1
    i += 1
    if not 0 <= i < len(instr):
        if states[1-current_program] == "done":
            break # both done
        states[current_program] = "done"
        indices[current_program] = i  # swap back since other program's not done
        current_program = 1 - current_program
        i = indices[current_program]
        d = ds[current_program]

print("Day 18 part 2:", total_sent)
