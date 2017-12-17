import progressbar

spinlock = [0]
step_size = 355
current_position = 0

for i in range(1, 2018):
    next_pos = (current_position + step_size) % len(spinlock)
    current_position = next_pos + 1
    spinlock.insert(current_position, i)

print("Day 17 part 1:", spinlock[spinlock.index(2017) + 1])

current_position = 0
spinlock_len = 1
val = 0


bar = progressbar.ProgressBar()

for i in bar(range(1, 50000000)):
    next_pos = (current_position + step_size) % spinlock_len
    current_position = next_pos + 1
    spinlock_len += 1
    if current_position == 1:
        val = i

print("Day 17 part 2:", val)
