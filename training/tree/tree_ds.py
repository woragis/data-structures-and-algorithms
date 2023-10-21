class BinaryNode:
    def __init__(self, data: int) -> None:
        self.node: int = data
        self.left: None | BinaryNode = None
        self.right: None | BinaryNode = None


class BinaryTree:
    def __init__(self, data: int) -> None:
        self.root: None | BinaryNode = BinaryNode(data)

    def insert(self, data):
        if not self.root:
            self.root = BinaryNode(data)
        else:
            self._in(data, self.root)

    def _in(self, data: int, cur_node: BinaryNode):
        if cur_node.node < data:
            if cur_node.left:
                self._in(data, cur_node.left)
            else:
                cur_node.left = BinaryNode(data)
        elif cur_node.node >= data:
            if cur_node.right:
                self._in(data, cur_node.right)
            else:
                cur_node.right = BinaryNode(data)

    def bfsTraverse(self):
        queue = [self.root]
        while len(queue) > 0:
            cur_node = queue.pop()
            print(cur_node.node)
            if cur_node.left:
                queue.insert(0, cur_node.left)
            if cur_node.right:
                queue.insert(0, cur_node.right)

    def dfsTraverse(self):
        stack = [self.root]
        while len(stack) > 0:
            cur_node = stack.pop()
            print(cur_node.node)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

    # def updateNode(self, node, new_value):


def randomNumberArray(arr, range_int, max_length):
    from random import randint
    for n in range(max_length):
        arr.append(randint(0, range_int))


if __name__ == '__main__':
    treeValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    newTree = BinaryTree(0)
    treeV = []
    randomNumberArray(treeV, 100, 20)
    for n in treeValues:
        newTree.insert(n)
    newTree.bfsTraverse()
