def mergeSort(arr):
    if len(arr) > 1:
        # get mid
        mid = len(arr)//2
        # separate arrays to left mid and right mid
        L = arr[:mid]
        R = arr[mid:]
        # recursion with separate arrays
        mergeSort(L)
        mergeSort(R)
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def merge2(arr):
    # divide and conquer

    # o(nlogn) time
    # o(n) space

    # 1. split array in half
    # 2. call merge sort each half to sort the recursevely
    # 3. merge both sorted halves into one sorted array
    if len(arr) > 1:
        middle = len(arr)//2  # define half
        left_arr = arr[:middle]  # first half
        right_arr = arr[middle:]  # second half
        merge2(left_arr)  # recursion
        merge2(right_arr)  # recursion
        # merge
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # keeps track of the index in the merged array
        # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        # check if the left array has anything to be inserted in the merged array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        # check if the right array has anything to be inserted in the merged array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def merge3(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge3(left_arr)
        merge3(right_arr)
        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def merge4(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge4(left_arr)
        merge4(right_arr)
        i, j, k = 0, 0, 0
        # iterate through all the subarrays
        while i < len(left_arr) and j < len(right_arr):
            # implement left[i] if it's smaller
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            # implement right[j] if it's smaller
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        # check if there was any element left in the smaller sub array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        # check if there was any element left in the bigger sub array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def randomArray(arr: list, limit: int):
    from random import randint
    for n in range(limit):
        new_ = randint(0, 100)
        arr.append(new_)
    print(arr)


myArr = [532, 234, 543, 23, 6548, 432, 520, 52,
         1209, 5, 5423, 52, 12, 1, -1552, 12, -15]
newList = []
randomArray(newList, 30)
merge2(newList)
print(newList)
