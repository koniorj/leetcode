# You are given an array of strings nums and an integer k. Each string in nums represents an integer 
# without leading zeros.

# Return the string that represents the kth largest integer in nums.

# Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], 
# "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.


def kthLargestNumber(nums, k):
    n = len(nums)
    if k > n:
        return None
    
    arr = []
    for i in range(n):
        arr.append(int(nums[i]))

    def partition(left, right, pid):
        i = left
        piv = arr[pid]
        arr[pid], arr[right] = arr[right], arr[pid]

        for j in range(left, right):
            if arr[j] > piv:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
            
        arr[i], arr[right] = arr[right], arr[i]
        return i
    
    def quickselect(left, right, k):
        while left <= right:
            piv = (left + right) // 2
            pivot = partition(left, right, piv)
            if k == pivot:
                return arr[pivot]
            elif k < pivot:
                right = pivot - 1
            else:
                left = pivot + 1
        # return arr[left]
    
    return str(quickselect(0, len(arr) - 1, k - 1))

nums = ["3","6","7","10"]
k = 4
print(kthLargestNumber(nums, k))