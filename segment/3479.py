# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents 
# the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with a capacity greater than 
# or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.

class SegmentTree:
    def __init__(self, size):
        self.unused = 0
        self.s = size
        self.n = 1
        while self.n < size:
            self.n *= 2
        self.tree = [0] * (2 * self.n)

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        idx //= 2
        while idx > 0:
            self.tree[idx] = max(self.tree[2*idx], self.tree[2*idx + 1])
            idx //= 2

    def query(self, val):
        curr = 1
        if val > self.tree[curr]:
            self.unused += 1
            return None
        while curr < self.n:
            if self.tree[curr*2] >= val:
                curr = curr*2
            elif self.tree[curr*2 + 1] >= val:
                curr = curr*2 + 1
            else:
                return None

        return curr - self.n 

def numOfUnplacedFruits(fruits, baskets):
    n = len(baskets)
    seg = SegmentTree(n)

    for i, val in enumerate(baskets):
        seg.update(i, val)

    for f in fruits:
        idx = seg.query(f)
        if idx is not None:
            seg.update(idx, 0)

    return seg.unused