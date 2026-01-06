import numpy as np, hashlib

class CountMinSketch:
    def __init__(self, d=5, w=1000):
        self.d, self.w = d, w
        self.table = np.zeros((d, w), dtype=np.int64)

    def _hash(self, x, i):
        h = hashlib.md5((str(x)+'|'+str(i)).encode()).hexdigest()
        return int(h, 16) % self.w

    def update(self, x, count=1):
        for i in range(self.d):
            self.table[i, self._hash(x, i)] += count

    def estimate(self, x):
        return min(self.table[i, self._hash(x, i)] for i in range(self.d))
