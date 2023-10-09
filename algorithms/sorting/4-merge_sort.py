def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # finding mid of the array
        L = arr[:mid]  # creating first half
        R = arr[mid:]  # creating second half
        mergeSort(L)  # sorting first half
        mergeSort(R)  # sorting second half

        i, j, k = 0, 0, 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    # code to print
    # code to print the list
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    # Driver code
    myArray = [2, 3, 2, 34, 24, 67, 45, 16]
    print(f'Given Array:')
    printList(myArray)
    mergeSort(myArray)
    print(f'\nSorted Array')
    printList(myArray)
