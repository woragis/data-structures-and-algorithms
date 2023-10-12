class Node:
    def __init__(self, data=None) -> None:
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data):
        cur = self.head
        new_node = Node(data)
        cur.prev = new_node
        while cur.next:
            cur = cur.next
        new_node.prev = cur
        cur.next = new_node

    def readNormal(self):
        cur = self.head
        elems = []
        while cur.next:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
        return

    def readLast(self):
        cur = self.head
        elems = []
        while cur.prev != self.head:
            cur = cur.prev
            elems.append(cur.data)
        cur = cur.prev
        print(elems)


myLL = DoublyLinkedList()
myLL.append(1)
myLL.append(2)
myLL.append(3)
myLL.append(4)
myLL.readNormal()
myLL.readLast()
