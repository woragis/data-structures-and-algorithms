def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    myArr = [64, 25, 12, 22, 11]
    print('Array:')
    print(myArr)
    selectionSort(myArr)
    print(myArr)
