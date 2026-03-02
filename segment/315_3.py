class SegmentTree:
    def __init__(self, size):
        self.n = 1
        while self.n < size:
            self.n *= 2
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        i += self.n
        self.tree[i] += val
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            i //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        res = 0

        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res
    
def countSmaller(nums):
    res = []

    sorted_unique = sorted(nums)
    val_to_idx = {}
    idx = 0
    for val in sorted_unique:
        if val not in val_to_idx:
            val_to_idx[val] = idx
            idx += 1

    m = len(sorted_unique)
    seg = SegmentTree(m)
    for num in reversed(nums):
        i = val_to_idx[num]
        if i > 0:
            count = (seg.query(0, i-1))
        else:
            count = 0
        res.append(count)
        seg.update(i, 1)

    res.reverse()
    return res

nums = [5, 2, 6, 1]
print(countSmaller(nums)) 