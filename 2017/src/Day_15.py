import progressbar as pbar


class Generator(object):
    def __init__(self, factor, start_value):
        self.factor = factor
        self.value = start_value
        self.divider = 2147483647

    def next(self):
        self.value = (self.factor*self.value) % self.divider
        return bin(self.value)


bar = pbar.ProgressBar()
gen_a = Generator(16807, 591)
gen_b = Generator(48271, 393)
count = 0
for i in bar(range(40000000)):
    if gen_a.next()[-16:] == gen_b.next()[-16:]:
        count += 1
print(count)

