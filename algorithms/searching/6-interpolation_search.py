def _interpolationSearch(arr, key, low, high):
    if low <= high and key >= arr[low] and key <= arr[high]:
        pos = low((high-low) // (arr[high]-arr[low]) * (key-arr[low]))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            return _interpolationSearch(arr, key, pos+1, high)
        if arr[pos] > key:
            return _interpolationSearch(arr, key, low, pos-1)
    return -1


def interpolationSearchRecursive(arr, key):
    low, high = 0, len(arr)-1
    return _interpolationSearch(arr, key, low, high)


def interpolationSearchIterative(arr, key):
    low, high = 0, len(arr)-1
    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            if arr[low] == key:
                return low
            return -1
        pos = int(
            low + (((float(high - low)/(arr[high]-arr[low])) * (key - arr[low]))))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            low = pos+1
        else:
            high = pos-1
    return -1
