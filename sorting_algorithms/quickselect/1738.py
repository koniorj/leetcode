# You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

# The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m 
# and 0 <= j <= b < n (0-indexed).

# Find the kth largest value (1-indexed) of all the coordinates of matrix.

def kthLargestValue(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    xor_arr = [[0 for _ in range(m)] for _ in range(n)]
    xor_arr[0][0] = matrix[0][0]

    arr = []
    for i in range(n):
        for j in range(m):
            if i > 0:
                matrix[i][j] ^= matrix[i-1][j]
            if j > 0:
                matrix[i][j] ^= matrix[i][j-1]
            if i > 0 and j > 0:
                matrix[i][j] ^= matrix[i-1][j-1]
            arr.append(matrix[i][j])

    # quickselect wywala podobno TLE 
    def partition(left, right, pid): # pid - pivot index
        i = left
        piv = arr[pid]
        arr[pid], arr[right] = arr[right], arr[pid]

        for j in range(left, right):
            if piv < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]
        return i

    import random
    def quickselect(left, right, k):
        while left < right:
            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)
            if k == pivot:
                return arr[k]
            elif k < pivot:
                right = pivot - 1
            else:
                left = pivot + 1

    k -= 1
    quickselect(0, len(arr)-1, k)
    return arr[k]

matrix = [[5,2],[1,6]]
k = 1 # 7
m = 2 # 5
print(kthLargestValue(matrix, m))

def kthLargestValue(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    xor_arr = [[0 for _ in range(m)] for _ in range(n)]
    xor_arr[0][0] = matrix[0][0]

    import heapq
    hq = []
    arr = []
    for i in range(n):
        for j in range(m):
            if i > 0:
                matrix[i][j] ^= matrix[i-1][j]
            if j > 0:
                matrix[i][j] ^= matrix[i][j-1]
            if i > 0 and j > 0:
                matrix[i][j] ^= matrix[i-1][j-1]
            arr.append(matrix[i][j])

    for num in arr:     
        if len(hq) < k:
            heapq.heappush(hq, num)
        elif hq[0] < num:
            heapq.heapreplace(hq, num)
        else:
            continue

    return hq[0]