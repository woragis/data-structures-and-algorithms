class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value already in the tree')

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return False


def fillTree(tree, num_elements=100, max_int=1000):
    from random import randint
    for _ in range(num_elements):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


myTree = BinarySearchTree()
# myTree = fillTree(myTree)
myTree.insert(23)
myTree.insert(22)
myTree.insert(21)
myTree.insert(12)
myTree.insert(8)

myTree.print_tree()
print(f'Tree height: {myTree.height()}')
print(myTree.search(8))
