def shellSort(arr):
    size = len(arr)
    gap = size//2
    while gap > 0:
        j = gap
        while j < size:
            i = j-gap
            while i >= 0:
                if arr[i+gap] > arr[i]:
                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                i = i-gap
            j += 1
        gap //= 2


array = [1, 58, 52, 48, 52, 25, 63, 21, 35, 58, 60, 10, 50, 52]
print(array)
shellSort(array)
print(array)
