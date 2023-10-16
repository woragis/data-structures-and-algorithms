def bubbleSort(arr):
    arr_size = len(arr)
    last_index = arr_size-1
    for i in range(arr_size):
        swapped = False
        for j in range(last_index-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break


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


def bubble2(arr):
    size = len(arr)
    index = len(arr)-1
    for i in range(size):
        swapped = False
        for j in range(index-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


randomArray = randomArr(50)
print('My random array:')
printarr(randomArray)
bubble2(randomArray)
print('\nMy sorted array:')
printarr(randomArray)
