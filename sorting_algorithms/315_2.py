class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, val):
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & (-i)

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res


def countSmaller(nums):
    sorted_unique = sorted(nums)
    val_to_idx = {}
    idx = 0
    for val in sorted_unique:
        if val not in val_to_idx:
            val_to_idx[val] = idx
            idx += 1

    n = len(val_to_idx)
    bit = BIT(n)
    res = []

    for num in reversed(nums):
        i = val_to_idx[num]
        res.append(bit.query(i-1))
        bit.update(i, 1)

    res.reverse()
    return res

nums = [5, 2, 6, 1]
print(countSmaller(nums)) 