class TernaryNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.mid = None
        self.right = None


class TernaryTree:
    def __init__(self, data) -> None:
        self.root = TernaryNode(data)

    def insert(self, data):
        cur_root = self.root
        new_node = TernaryNode(data)
        while True:
            if not cur_root.left:
                cur_root.left = new_node
                return
            elif not cur_root.mid:
                cur_root.mid = new_node
                return
            elif not cur_root.right:
                cur_root.right = new_node
                return
            else:
                cur_root = cur_root.left


class BinaryNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data: int) -> None:
        self.root = BinaryNode(data)
    # implementation

    def insert(self, value: int):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node: BinaryNode, value: int):
        if value < cur_node.data:
            if not cur_node.left:
                cur_node.left = BinaryNode(value)
            else:
                self._insert(cur_node.left, value)
        elif value > cur_node.data:
            if not cur_node.right:
                cur_node.right = BinaryNode(value)
            else:
                self._insert(cur_node.right, value)

    def printTree(self):
        cur = self.root
        if cur:
            return self._printTree(cur)

    def _printTree(self, cur_node: BinaryNode):
        if cur_node:
            self._printTree(cur_node.left)
            print(str(cur_node.data))
            self._printTree(cur_node.right)

    def height(self):
        cur = self.root
        if not cur:
            return 0
        else:
            return self._height(cur, 0)

    def _height(self, cur_node: BinaryNode, cur_height: int):
        if not cur_node:
            return cur_height
        left_height = self._height(cur_node.left, cur_height+1)
        right_height = self._height(cur_node.right, cur_height+1)
        return max(left_height, right_height)

    def search(self, target):
        if self.root:
            return self._search(self.root, target)
        else:
            return False

    def _search(self, cur_node: BinaryNode, target):
        if target == cur_node.data:
            return True
        elif target < cur_node.data and cur_node.left:
            return self._search(cur_node.left, target)
        elif target > cur_node.data and cur_node.right:
            return self._search(cur_node.right, target)
        return False

    # ALGORITHMS:

    def depthFirstSearch(self):
        # depth first search traversal
        # stack
        # time complexity: O(n) -> n = number of nodes
        # space complexity: O(n)
        cur = self.root
        if cur:
            stack = [cur]
        else:
            return []
        result = []
        while stack:
            current_node = stack.pop()
            result.append(current_node)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        print(result)
        return result

    def depthRecursive(self):
        return self._depthRecursive(self.root)

    def _depthRecursive(self, root):
        if not root:
            return []
        result = [root]
        left_values = self._depthRecursive(self.root.left)
        for i in left_values:
            result.append(i)
        right_values = self._depthRecursive(self.root.right)
        for i in right_values:
            result.append(i)
        return result

    def breadthTraversal(self):  # iterative is the best for it
        # time complexity: O(n)
        # space complexity: O(n)
        cur = self.root
        if not cur:
            return []
        queue = [cur]
        result = [cur]
        for node in queue:
            if node.left:
                queue.append(node.left)
                result.append(node.left)
            if node.right:
                queue.append(node.right)

    def valueInBinaryTree(self, target):
        cur = self.root
        if not cur:
            return False

        return False

    def treeIncludes(self, target: int):  # iterative DFs
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.data == target:
                return True
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def treeIncludes(self, target) -> bool:
        if not self.root:
            return False
        else:
            return self._treeIncludes(self.root, target)

    def _treeIncludes(self, root: BinaryNode, target: int) -> bool:  # recursive DFS
        if not root:
            return False
        if root.data == target:
            return True
        return self._treeIncludes(root.left, target) or self._treeIncludes(root.right, target)

    def treeSum(self) -> int:  # recursive
        if not self.root:
            return 0
        return self._treeSum(self.root)

    def _treeSum(self, root: BinaryNode) -> int:
        if not root:
            return 0
        return root.data + self._treeSum(root.left) + self._treeSum(root.right)

    def treeSum_(self):
        if not self.root:
            return 0
        queue = [self.root]
        total_sum = 0
        while queue:
            current = queue.pop(0)
            total_sum += current.data
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return total_sum


def fillTree(tree: BinaryTree, num_elements: int = 100, max_int: int = 1000):
    from random import randint
    for _ in range(num_elements):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


if __name__ == '__main__':
    MyNewTree = BinaryTree(1)
    MyNewTree = fillTree(MyNewTree, 200, 10000)
    MyNewTree.printTree()
    sum = MyNewTree.treeSum()
    print(sum)
    exit()
