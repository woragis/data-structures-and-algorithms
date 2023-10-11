print('Matrix: https://www.geeksforgeeks.org/matrix/')


def searchMatrix(matrix, key):
    visited = set()
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            pos = f'{row},{column}'
            if pos in visited:
                continue
            visited.add(pos)
            if matrix[row][column] == key:
                return pos
    return -1


def searchMatriIterative(matrix, key):
    # visited_set = set()
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            # pos = f'{row},{column}'
            # if pos in visited_set:
            #     continue
            # visited_set.add(pos)
            if matrix[row][column] == key:
                return pos
    return -1


def matrixDiagonal(matrix):
    main_d = []
    secondary_d = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row == column:
                main_d.append(matrix[row][column])
            if row == abs((column-len(matrix)))-1:
                secondary_d.append(matrix[row][column])
    return [main_d, secondary_d]


def matrixSort(matrix):
    n = len(matrix)
    temp = [0]*n*n
    k = 0
    for i in range(0, n):
        for j in range(0, n):
            temp[k] = matrix[i][j]
            k += 1
    temp.sort(reverse=True)
    k = 0
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = temp[k]
            k += 1


def reverseColumns(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])
    for i in range(column_length):
        for j in range(0, int(column_length/2)):
            matrix[j][i], matrix[column_length-1 -
                                 j][i] = matrix[column_length-1-j][i], matrix[j][i]


def transpose(matrix: list[list]):
    row_length = len(matrix)
    column_length = len(matrix[0])
    for row in range(row_length):
        for column in range(row, column_length):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]


def rotateMatrix180(matrix):
    transpose(matrix)
    reverseColumns(matrix)
    transpose(matrix)
    reverseColumns(matrix)


def unique(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])
    maximum = 0
    flag = 0
    for row in range(row_length):
        for column in range(column_length):
            if maximum < matrix[row][column]:
                maximum = matrix[row][column]
    b = [0]*(maximum+1)
    for row in range(row_length):
        for column in range(column_length):
            y = matrix[row][column]
            b[y] += 1
    for i in range(1, maximum+1):
        if b[i] == 1:
            print(i, end=' ')
    flag = 1
    if flag == 0:
        print('no unique elements in matrix')


if __name__ == '__main__':
    myMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # pos = searchMatrix(myMatrix, 8)
    # diagonals = matrixDiagonal(myMatrix)
    # print(pos)
    # print(diagonals)
    print(myMatrix)
    rotateMatrix180(myMatrix)
    unique(myMatrix)
    print(myMatrix)
