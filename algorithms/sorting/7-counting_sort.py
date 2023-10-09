def countingSort(arr):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    ans = ['' for _ in arr]
    for i in arr:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]

    return ans


if __name__ == '__main__':
    # myArr = [255, 4382, 452, 42, 2432, 2482, 462, 42, 42]
    myArr = 'geeksforgeeks'
    print(myArr)
    ans = countingSort(myArr)
    print('Sorted arr is %s' % (''.join(ans)))
