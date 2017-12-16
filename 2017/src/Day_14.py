from PIL import Image
import random
import progressbar as pbar


from Day_10 import knot_hash


class ImageCreator(object):
    """ Image creator for visualizations for problem 2017 Day 14 part 2.
    """
    def __init__(self, dir_path=""):
        """Constructor
        :param dir_path: path to output directory.
        """
        self.count = 0
        self.path = dir_path

    def to_pdf(self, array):
        """ Generates a 128x128 .png file based on RGB tuples in array.
        :param array: Array with length 128*128 (16384) with RGB tuples.
        :return:
        """
        if len(array) != 128*128:
            raise AttributeError(f'Array was wrong size. Found {len(array)}, should be 16384')
        img = Image.new('RGB', (128, 128))
        img.putdata(array)
        img.save(f'{self.path}/image-{self.count}.png')
        self.count += 1


class Day14(object):
    def __init__(self, key, img_creator=None, save_by_element=False):
        """
        Solves problems from 2017 day 14.
        :param key: input key.
        :param img_creator: Optional reference to ImageCreator for creation of visualizations.
        :param save_by_element: Boolean decider to choose how often an image is created if ImageCreator is given.
        False will render one image per group found. True will render one image per element.
        """
        self.hashes = []
        self.img_array = None
        self.img_creator = img_creator
        self.save_by_element = save_by_element

        for i in range(128):
            key_string = key + "-" + str(i)
            h = knot_hash(key_string)
            b = [bin(int(c, 16))[2:].zfill(4) for c in h]
            b = "".join(b)
            self.hashes.append([int(c) for c in list(b)])
        if self.img_creator:
            self.img_array = []
            for i in range(len(self.hashes)):
                for j in range(len(self.hashes[0])):
                    if self.hashes[i][j] == 1:
                        self.img_array.append((255, 255, 255))
                    else:
                        self.img_array.append((0, 0, 0))
            self.img_creator.to_pdf(self.img_array)

    def sum_matrix(self):
        return sum(map(sum, self.hashes))

    def remove_group(self, x, y, color=None):
        """Recursively removes group of location x, y.
        :param x: int x coordinate of element for which the group should be removed.
        :param y: int y coordinate of element for which the group should be removed.
        :param color: RGB tuple representing the color of the group being removed. Ex: (255, 255, 255) = white.
        """
        n_locs = [(x, max(0, y - 1)), (min(x + 1, len(self.hashes) - 1), y), (x, min(y + 1, len(self.hashes) - 1)), (max(x - 1, 0), y)]
        self.hashes[x][y] = 0
        if self.img_creator and color:
            self.img_array[x*len(self.hashes)+y] = color
            if self.save_by_element:
                self.img_creator.to_pdf(self.img_array)
        for loc in n_locs:
            if self.hashes[loc[0]][loc[1]] == 1:
                self.remove_group(loc[0], loc[1], color)

    def solve(self):

        print("Day 14 part 1:", self.sum_matrix())

        # Image creation takes a while so I chose to add a progress bar if this option is used.
        if self.img_creator:
            bar = pbar.ProgressBar()
            region_count = 0
            for i in bar(range(len(self.hashes))):
                for j in range(len(self.hashes[0])):
                    if self.hashes[i][j] == 1:
                        group_color = (random.randrange(256), random.randrange(256), random.randrange(256))
                        self.remove_group(i, j, group_color)
                        if self.img_creator and not self.save_by_element:
                            self.img_creator.to_pdf(self.img_array)
                        region_count += 1
        else:
            region_count = 0
            for i in range(len(self.hashes)):
                for j in range(len(self.hashes[0])):
                    if self.hashes[i][j] == 1:
                        self.remove_group(i, j)
                        region_count += 1

        print("Day 14 part 2:", region_count)


day_14 = Day14(key=open("../inputs/Day_14.txt").readline())
day_14.solve()
