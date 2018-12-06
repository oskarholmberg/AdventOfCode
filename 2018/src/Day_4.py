import re
import operator
from collections import defaultdict

lines = open('../inputs/Day_4.txt').read().split('\n')
lines.sort()

C = defaultdict(int)
CM = defaultdict(int)
guard = None
asleep = None
for line in lines:
    if line:
        time= int(re.findall(r':(\d+)', line)[0])
        if 'begins shift' in line:
        	guard = int(re.findall(r'#(\d+)', line)[0])
        	asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for t in range(asleep, time):
                CM[(guard, t)] += 1
                C[guard] += 1

def argmax(d):
    k = max(d, key=d.get)
    return key, d[k]

sleepiest_guard = max(C, key=C.get)

sleepiest_min = [CM[(sleepiest_guard, k)] for k in range(60)].index(max([CM[(sleepiest_guard, k)] for k in range(60)]))

print(f'Part 1: {sleepiest_guard*sleepiest_min}')

best_guard, best_min = max(CM, key=CM.get)

print(f'Part 2: {best_guard*best_min}')