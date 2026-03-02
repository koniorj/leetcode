# You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

# You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. 
# For each queries[i], you need to:

# Trim each number in nums to its rightmost trimi digits.
# Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, 
# the number with the lower index is considered to be smaller.
# Reset each number in nums to its original length.
# Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.

def smallestTrimmedNumbers(nums, queries):
    # nums to tablica stringow, dlatego w kazdym wywolaniu partition bedziemy zamieniac stringi na liczby
    def partition(arr, left, right, pid):
        i = left
        piv = arr[pid]
        arr[pid], arr[right] = arr[right], arr[pid]

        for j in range(left, right):
            if arr[j] < piv:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]
        return i
    
    def quickselect(arr, left, right, k):
        while left <= right:
            piv = (left+right) // 2
            pivot = partition(arr, left, right, piv)
            if k == pivot:
                return arr[pivot]
            elif k < pivot:
                right = pivot-1
            else:
                left = pivot+1
        return arr[k]

    ans = []
    n = len(nums)
    for k, trim in queries:
        trimmed = [num[-trim:] for num in nums]
        trimmed_id = [(trimmed[i], i) for i in range(n)]
        val, i = quickselect(trimmed_id, 0, n-1, k-1)
        ans.append(i)

    return ans

nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]
print(smallestTrimmedNumbers(nums, queries))