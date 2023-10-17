'''
# pivot:
# 1. correct position in final, sorted array
# 2. items to the left are smaller
# 3. items to the right are larger
from random import randint


class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:

        def quicksort(nums, lo, hi):
            if lo < hi:
                partition_resting_point = partition(nums, lo, hi)
                quicksort(nums, lo, partition_resting_point - 1)
                quicksort(nums, partition_resting_point + 1, hi)

        def partition(nums, lo, hi):
            pivotIdx = randint(lo, hi)
            nums[pivotIdx], nums[hi] = nums[hi], nums[pivotIdx]
            pivot = nums[hi]

            l_idx = lo
            r_idx = hi-1
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

        quicksort(nums, 0, len(nums)-1)
        return nums


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high], arr[high], arr[i+1]
    return i+1


def quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick(arr, low, pi-1)
        quick(arr, pi+1, high)

def partition(arr, row, high):
    pivot = arr[high]
def q(arr, low, high):
    return
'''


def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)


def partition(arr, left, right):
    i, j = left, right-1
    pivot = arr[right]
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


if __name__ == '__main__':
    # best yt tutorial:
    # https://www.youtube.com/watch?v=9KBwdDEwal8&ab_channel=FelixTechTips
    myArr = [10, 7, 8, 9, 10, 15, 58, 23]
    N = len(myArr)
    print('Array:')
    print(myArr)
    quicksort(myArr, 0, len(myArr)-1)
    print('Sorted Array:')
    print(myArr)
