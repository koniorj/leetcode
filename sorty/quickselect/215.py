def partition(arr, left, right):
    # pivot = (left + right) // 2
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


def quickselect(arr, k, left, right):
    if left <= right:
        pivot = partition(arr, left, right)

        if pivot == k:
            return arr[pivot]
        elif pivot < k:
            return quickselect(arr, k, pivot+1, right)
        else:
            return quickselect(arr, k, left, pivot-1)