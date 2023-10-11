def _ternarySearch(arr, key, l, r):
    if r >= l:
        mid1 = l+(r-l)//3
        mid2 = r-(r-l)//3
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            return _ternarySearch(arr, key, l, mid1-1)
        elif key > arr[mid2]:
            return _ternarySearch(arr, key, mid2+1, r)
        else:
            return _ternarySearch(arr, key, mid1+1, mid2-1)
    return -1


def ternarySearch(arr, key):
    l, r = 0, len(arr)-1
    return _ternarySearch(arr, key, l, r)


if __name__ == '__main__':
    myRandomArr = [1, 2, 3, 4, 5, 8, 9, 12, 23, 34,
                   45, 56, 67, 89, 129, 234, 452, 521, 2356]
    index = ternarySearch(myRandomArr, 67)
    print(index)
