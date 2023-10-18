def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i, k = i+1, k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j, k = j+1, k+1


myArr = [5, 4, 3, 7, 8, 9, 2, 1, 10]
print(myArr)
mergeSort(myArr)
print(myArr)
