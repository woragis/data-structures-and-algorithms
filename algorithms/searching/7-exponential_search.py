def _binarySearch(arr, key, left, right):
    if left <= right:
        mid = left + (right-left) // 2

        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return _binarySearch(arr, key, left, mid-1)
        return _binarySearch(arr, key, mid+1, right)
    return -1


def exponentialSearch(arr, key):
    n = len(arr)
    if arr[0] == key:
        return 0
    i = 1
    while i < n and arr[i] <= key:
        i *= 2

    return _binarySearch(arr, key, i//2, min(i, len(arr)-1))
