class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, value):
        cur = self.root
        while cur.next:
            cur = cur.next
            if cur == self.root:
                break
        cur.next = Node(value)
        cur.next.prev = cur
        self.root.prev = cur.next

    def traverse(self):
        cur = self.root
        while cur.next:
            cur = cur.next
            if cur == self.root:
                break
            print(cur.data)

    def reverseTraverse(self):
        cur = self.root
        while cur.prev:
            cur = cur.prev
            if cur == self.root:
                break
            print(cur.data)

    def update(self, target, new_value):
        cur = self.root
        while cur.next:
            cur = cur.next
            if cur.data == target:
                cur.data = new_value
                break

    def delete(self, target):
        cur = self.root
        last = cur
        while cur.next:
            last = cur
            cur = cur.next
            if cur.data == target:
                temp = cur.next
                last.next = cur.next
                temp.prev = cur.prev
            if cur == self.root:
                break


if __name__ == '__main__':
    myDLL = DoublyLinkedList()
    myDLL.insert(15)
    myDLL.insert(16)
    myDLL.insert(17)
    myDLL.insert(18)
    myDLL.delete(15)
    myDLL.delete(16)
    myDLL.reverseTraverse()
    # myDLL.reverseTraverse()
