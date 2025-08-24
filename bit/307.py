# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices 
# left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n+1) # indeksowanie od 1
        self.nums = nums[:] # musi byc kopia bo leetcode sprawdzi dosl tablice nums

        for i, v in enumerate(nums):
            self.update(i, v)
        
    def update(self, index, val):
        diff = val - self.nums[index] 
        self.nums[index] = val
        self.add(index+1, diff)
 
    def add(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += index & -index

    def query(self, index):
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= index & -index
        return ans

    def sumRange(self, left, right):
        return self.query(right+1) - self.query(left)