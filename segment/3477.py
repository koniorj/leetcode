# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] 
# represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with a capacity greater than or 
# equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.

class SegmentTree:
    def __init__(self, baskets):
        n = len(baskets)
        self.size = 1
        self.unused = 0
        while self.size < n:
            self.size *= 2 # self.size to ilosc lisci w drzewie :)
        self.tree = [0] * 2 * self.size # tutaj zaraz damy rozmiary tych basketow

        for i in range(n):
            self.tree[self.size + i] = baskets[i] 

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def query(self, val): # jaki jest najbardziej po lewej koszyk do ktorego sie zmiesci nasz owoc?
        i = 1
        if val > self.tree[i]:
            self.unused += 1
            return None
        while i < self.size:
            if self.tree[i*2] >= val: 
                i = i*2
            else:
                i = i*2+1

        return i - self.size # na luziku sie zmiesci
    
    def add(self, idx):
        # wczesniej zadajemy pytanie gdzie sie zmiesci, dostajemy indeks
        i = idx + self.size
        self.tree[i] = 0
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])
            i //= 2

def numOfUnplacedFruits(fruits, baskets):
    seg = SegmentTree(baskets)

    # juz mamy w seg rozmiary koszykow. Teraz zostalo tylko umiescic owoce
    for vol in fruits: # volume
        i = seg.query(vol)
        if i is not None:
            seg.add(vol, i)

    return seg.unused

fruits = [4,2,5]
baskets = [3,5,4]
print(numOfUnplacedFruits(fruits, baskets))