# Given an integer array nums, return the maximum difference between two successive 
# elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        mini = min(nums)
        maxi = max(nums)
        if mini == maxi:
            return 0

        gap = max(1, (maxi-mini)//(n-1))

        buckets = [[None, None] for _ in range((maxi-mini)//gap+1)]

        for num in nums:
            i = (num - mini) // gap
            if buckets[i][0] is None:
                buckets[i][0] = buckets[i][1] = num
            else:
                buckets[i][0] = min(num, buckets[i][0])
                buckets[i][1] = max(num, buckets[i][1])

        biggest_gap = 0
        prev_gap = mini
        for bucket in buckets:
            if bucket[0] is not None:
                biggest_gap = max(biggest_gap, bucket[0] - prev_gap)
                prev_gap = bucket[1]

        return biggest_gap
    
solution = Solution()
print(solution.maximumGap([3, 6, 9, 1]))