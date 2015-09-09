# by Dmitriy Nyashkin https://github.com/fdcore
# Inspired https://github.com/zackkitzmiller/tiny-php

import math

class Tiny:

    set = "" # secret key

    # init secret key
    def __init__(self, set):
        self.set = set

    # Encode int to string
    def encode(self, id):
        set = self.set

        hexn = ''
        try:
            id = int(math.floor(abs(int(id))))
            radix = len(set)
            while True:
                r = id % radix
                hexn = set[r] + hexn;
                id = (id - r) / radix;
                if id == 0:
                    break
        except ValueError, e:
            return None

        return hexn

    # Decode string to int
    def decode(self, s):
        set = self.set
        s = str(s)
        radix = len(set)
        strlen = len(s)
        n = 0

        try:
            for i in range(0, strlen):
                n += set.index(s[i]) * math.pow(radix, (strlen - i - 1))
        except ValueError, e:
            return None

        return int(n)
        
    # Generate secret key
    def generate_set(self):
        import random
        arr = []
        for i in range(65, 123):
            if i < 91 or i > 96: arr.append(chr(i))
        for s in range(0, 10): arr.append(str(s))
        random.shuffle(arr)
        return "".join(arr)
