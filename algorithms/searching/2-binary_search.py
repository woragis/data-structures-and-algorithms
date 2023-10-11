def binarySearch(arr, key):
    l, r = 0, len(arr)-1
    search = 0
    while l <= r:
        search += 1
        mid = l+(r-l)//2
        if arr[mid] == key:
            return [mid, search]
        elif arr[mid] < key:
            l = mid+1
        else:
            r = mid-1
    return [-1, search]


def createArray(length: int):
    array = []
    for i in range(length):
        array.append(i)
    return array


if __name__ == '__main__':
    my10Arr = createArray(10)
    my100Arr = createArray(100)
    my1000Arr = createArray(1000)
    my10000Arr = createArray(10000)
    my100000000Arr = createArray(100000000)
    res1 = binarySearch(my10Arr, 1)
    res2 = binarySearch(my100Arr, 1)
    res3 = binarySearch(my1000Arr, 1)
    res4 = binarySearch(my10000Arr, 1)
    res5 = binarySearch(my100000000Arr, 1)
    print(f'result in 10 arr: {res1}')
    print(f'result in 100 arr: {res2}')
    print(f'result in 1k arr: {res3}')
    print(f'result in 10k arr: {res4}')
    print(f'result in 100 millions arr: {res5}')
