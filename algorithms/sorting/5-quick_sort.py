def partition(array, low, high):
    pivot = array[high]
    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller from pivot is found
            # swap it with the greater element pointed by i
            i += 1

            # swaping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # swap the pivot element with
    # the greater element specified by i
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 10, 15, 58, 23]
    N = len(array)
    print('Array:')
    print(array)

    quickSort(array, 0, N-1)
    print('Sorted Array:')
    print(array)
