# You are given an array of people, people, which are the attributes of some people in 
# a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith 
# person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people. 
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is 
# the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2 # ilosc lisci
        self.tree = [0] * 2 * self.size # 1 -> wolne miejsce, 0 -> zajete
     
        for i in range(n):
            self.tree[self.size+i] = 1
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def query(self, k): # szukamy indeksu k-tego wolnego miejsca
        i = 1
        while i < self.size:
            if self.tree[i*2] > k:
                i = i*2
            # elif self.tree[i*2+1] > k:
            else:
                k -= self.tree[i*2]
                i = i*2+1

        return i - self.size
    
    def add(self, idx):
        i = idx + self.size
        self.tree[i] = 0
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
            i //= 2

def reconstructQueue(people):
    # tutaj segment tree to tablica wolnych miejsc. Cchcemy znajdowac k-ty wolny indeks
    n = len(people)
    seg = SegmentTree(n)
    # potrzebujemy posortowac ludzi. Rosnaco po wzroscie, malejaco po priorytecie
    people.sort(key=lambda x: (x[0], -x[1]))
    ans = [None] * (2*n)

    for h, k in people:
        i = seg.query(k)
        seg.add(i)
        ans[i] = [h, k]

    ans = [x for x in ans if x is not None]
    return ans

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
print(reconstructQueue(people))

people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
print(reconstructQueue(people))