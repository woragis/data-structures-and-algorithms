def bubbleSort(arr):
    n = len(arr)

    # traverse through all elements from the array
    for i in range(n):
        swapped = False

        # last i element are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # swap if the element found is greater
            # than next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break


if __name__ == '__main__':
    print('Time Complexity: O(N*N)')
    print('Space Complexity: O(1)')
    advantages = [
        'easy to understand and implement',
        'it does not require any additional memory space',
        'it is a stable sorting algorithm, meaning the elements with the same key value maintain their relative order in the sorted output'
    ]
    disadvantages = [
        'has time complexity of O(N*N) (very slow)',
        'comparison based algorithm, which means that it requires comparison operator to determine the relative order of the elements, in the input data set. (it can limit the algorithm in certain cases)'
    ]
    arr = [63, 54, 42, 42, 524, 15, 25, 4]
    print(arr)
    bubbleSort(arr)
    print(arr)
