def jumpSearch(arr, key):
    from math import sqrt
    n = len(arr)
    step = sqrt(n)
    prev = 0
    while arr[int(min(step, n)-1)] < key:
        prev = step
        step += sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < key:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == key:
        return prev
    return -1
