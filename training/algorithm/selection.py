def selectionSort(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def selectSort2(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def select3(arr):
    size = len(arr)
    for i in range(size):
        mi = i
        for j in range(i+1, size):
            if arr[j] < arr[mi]:
                mi = j
        arr[i], arr[mi] = arr[mi], arr[i]


def randomArr(arr_size):
    from random import randint
    randomArr = []
    for i in range(arr_size):
        randomArr.append(randint(0, 10000))
    return randomArr


def printarr(arr):
    for i in arr:
        print(i, end=' ')
    print()


myRandomArr = randomArr(20)
print('Random Array:')
printarr(myRandomArr)
select3(myRandomArr)
print('\nSelection Sorted Array:')
printarr(myRandomArr)
