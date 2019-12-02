import re
import numpy as np
import operator
from collections import defaultdict

lines = open('../inputs/Day_4.txt').read().split('\n')
lines.sort()

guards = defaultdict(int)
guards_by_minute = defaultdict(int)
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
                guards_by_minute[(guard, t)] += 1
                guards[guard] += 1

sleepiest_guard = max(guards, key=guards.get)

sleepiest_min = np.argmax([guards_by_minute[(sleepiest_guard, k)] for k in range(60)])

print(f'Part 1: {sleepiest_guard*sleepiest_min}')

best_guard, best_min = max(guards_by_minute, key=guards_by_minute.get)

print(f'Part 2: {best_guard*best_min}')