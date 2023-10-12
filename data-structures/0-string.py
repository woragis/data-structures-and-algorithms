def firstIndex(string: str, c: str) -> int:
    if string.index(c):
        index = string.index(c)
        return index
    return -1


def lastIndex(string: str, c: str) -> int:
    string, c = string[::-1], c[::-1]
    if string.index(c):
        index = string.index(c)
        return abs(index-len(string)+1)
    return -1


def reverseStringRecursive(string: str) -> str:
    ans = ""
    string = list(string)
    while string:
        current_last = string.pop()
        ans += current_last
    print(ans)
    return ans


def _leftRotate(string: str) -> str:
    lst = list(string)
    first_element = lst.pop(0)
    lst.append(first_element)
    string = ''.join(lst)
    return string


def leftRotate(string: str, times: int) -> str:
    while times:
        times -= 1
        string = _leftRotate(string)
    return string


def _rightRotate(string: str) -> str:
    lst = list(string)
    last_element = lst.pop()
    lst.insert(0, last_element)
    string = ''.join(lst)
    return string


def rightRotate(string: str, times: int) -> str:
    while times:
        times -= 1
        string = _rightRotate(string)
    return string

# rotation without being recursive/iterative
# sort string
# print frequency of each character in alphabetical order
# swap characters in string
# insert characters in a string at a certain position
# check if two strings are the same
# concatenating two strings
# remove all ocurrences of a character in a string

# substring and subsequence


if __name__ == '__main__':
    myString = 'Jezreel de Andrade Galvao Veloso'
    print(leftRotate(myString, 10))
