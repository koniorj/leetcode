# Given an integer array nums, return an integer array counts where counts[i] is the number
# of smaller elements to the right of nums[i].

def countSmaller(nums):
    n = len(nums)
    res = [0] * n

    enum = [(i, nums[i]) for i in range(n)]
    mergesort(enum, 0, n-1, res)
    return res

def mergesort(enum, start, end, res):
    if start >= end:
        return
    
    mid = (start + end) // 2
    mergesort(enum, start, mid, res)
    mergesort(enum, mid+1, end, res)
    merge(enum, start, mid, end, res)

def merge(enum, start, mid, end, res):
    p, q = start, mid+1
    inversions = 0
    temp = []

    while p <= mid and q <= end:
        if enum[p][1] <= enum[q][1]:
            temp.append(enum[p])
            res[enum[p][0]] += inversions
            p += 1
        else:
            temp.append(enum[q])
            inversions += 1
            q += 1

    while p <= mid:
        temp.append(enum[p])
        res[enum[p][0]] += inversions
        p += 1

    while q <= end:
        temp.append(enum[q])
        q += 1

    enum[start:end+1] = temp

nums = [5,2,6,1]
print(countSmaller(nums))