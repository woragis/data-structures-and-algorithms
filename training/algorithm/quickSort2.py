# version 1
def partition1(arr, left, right):
    pivot = arr[right]
    l_index = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            l_index += 1
            arr[l_index], arr[j] = arr[j], arr[l_index]
    arr[l_index+1], arr[right], arr[right], arr[l_index+1]

    return l_index+1


def quickSort1(arr, left, right):
    if left < right:
        pi = partition1(arr, left, right)
        quickSort1(arr, left, pi-1)
        quickSort1(arr, pi+1, right)

# version 2


def partition2(nums, lo, hi):
    pivot = nums[hi]
    l_idx, r_idx = lo, hi-1
    while l_idx <= r_idx:
        if nums[l_idx] <= pivot:
            l_idx += 1
        elif nums[r_idx] >= pivot:
            r_idx -= 1
        else:
            nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
            l_idx += 1
            r_idx -= 1
    nums[l_idx], nums[hi] = nums[hi], nums[l_idx]
    return l_idx


def quickSort2(nums, lo, hi):
    if lo < hi:
        partition_resting_point = partition2(nums, lo, hi)
        quickSort2(nums, lo, partition_resting_point-1)
        quickSort2(nums, partition_resting_point+1, hi)


# Definitive code
def partition(arr, left, right):
    pivot = arr[right]
    i, j = left, right-1
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


def quickSort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quickSort(arr, left, partition_pos-1)
        quickSort(arr, partition_pos+1, right)


myarr = [5, 2, 4, 7, 8, 9, 1, 3, 10]
print(myarr)
# mergeSort(myarr)
print(myarr)
