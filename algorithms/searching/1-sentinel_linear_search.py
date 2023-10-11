def sentinelSearch(arr, key):
    n = len(arr)
    last = arr[n-1]
    arr[n-1] = key
    i = 0
    while arr[i] != key:
        i += 1
    arr[n-1] = last
    if i < n-1 or arr[n-1] == key:
        print(f'{key} is present at index {i}')
        return i
    else:
        print('element not found')
        return -1


if __name__ == '__main__':
    myArr = [134, 452, 49, 94, 2, 423, 59, 857, 87, 5, 52]
    index = sentinelSearch(myArr, 49)
    print(index)
