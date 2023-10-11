def linearSearch(arr: list[any], key: any):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == '__main__':
    randomList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 23, 234]
    index = linearSearch(randomList, 23)
    print(index)
