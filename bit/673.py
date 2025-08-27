# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

class BIT:
    def __init__(self, m):
        self.size = m+1
        self.tree = [(0,0)] * (m+1)

    def query(self, i):
        best_len, cnt = 0, 0
        while i > 0:
            l, c = self.tree[i]
            if l > best_len:
                best_len = l
                cnt = c
            elif l == best_len:
                cnt += c
            i -= i & -i
        return best_len, cnt
    
    def update(self, i, l, c): # length i count
        while i < self.size:
            bl, bc = self.tree[i]
            if l > bl:
                self.tree[i] = (l, c)
            elif l == bl:
                self.tree[i] = (bl, bc+c)
            i += i & -i
        
def findNumberOfLIS(nums):
    # zadanie ma tag na BIT, wiec sprobujemy je nim rozwiazac (mimo ze DP jest duzo bardziej intuicyjne)
    if not nums:
        return 0

    # dlugosc BITu bedzie rowna dlugosci nums. Skompresujemy wartosci nums oczywiscie.
    # W danym indeksie bedziemy przechowywac najdluzszy LIS konczacy sie tutaj oraz cnt tych LIS-ow.
    values = sorted(set(nums))
    compressed = {v: i+1 for i,v in enumerate(values)} # indeksowanie od 1 jak zawsze
    m = len(values)
    bit = BIT(m)

    for num in nums:
        idx = compressed[num]
        curr_len, curr_cnt = bit.query(idx-1)
        if curr_cnt == 0:
            curr_cnt = 1
        bit.update(idx, curr_len+1, curr_cnt)

    return bit.query(m)[1]

print(findNumberOfLIS(nums=[1,3,5,4,7]))