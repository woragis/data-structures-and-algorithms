# searches in array:
# linear search, sentinel linear search, binary search, ternary_search

def reverseList(arr: list):
    start, end = 0, len(list)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverseListRecursive(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseListRecursive(arr, start+1, end-1)


def rightRotation(arr: list, times: int):
    while times > 0:
        first_element = arr.pop(0)
        arr.append(first_element)
        times -= 1
        rightRotation(arr, times)


def leftRotation(arr: list, times: int):
    while times > 0:
        last_element = arr.pop()
        arr.insert(0, last_element)
        times -= 1
        leftRotation(arr, times)


def jugglingRotation(arr: list):
    pass


def reverseAlgorithm(arr: list):
    arr = arr[::-1]


def linearSearchUnsorted(arr: list[any], target: any):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def insertUnsorted(arr: list[any], element: any):
    arr.append(element)


def insertElementUnsorted(arr: list[any], element: any, position: int):
    arr.insert(position, element)


def deleteElementUnsorted(arr: list[any], target: any):
    for i in range(len(arr)):
        if arr[i] == target:
            arr.pop(i)
            return
    return


def binarySearch(arr: list[any], target: any):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1


def binarySearchInsert(arr: list[int], element: int):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == element:
            for n in range(len(arr)-l):
                if arr[mid+n] == element:
                    continue
            arr.insert(mid+1, element)
            return
        elif element > arr[mid]:
            l = mid+1
        else:
            r = mid-1
    # if r == 1:


def deleteElement(arr: list, element):
    pos = binarySearch(arr, element)
    if pos == -1:
        return -1
    arr.pop(pos)


if __name__ == '__main__':
    myArr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(myArr)
    # print(binarySearch(myArr, 2))
    pos = deleteElement(myArr, 5)
'''
    print(myArr)
    rightRotation(myArr, 1)
    print(myArr)
    rightRotation(myArr, 1)
    print(myArr)
    leftRotation(myArr, 1)
    print(myArr)
    leftRotation(myArr, 1)
    print(myArr)
    leftRotation(myArr, 1)
    print(myArr)
'''
