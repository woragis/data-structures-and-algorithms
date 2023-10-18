# Linked List File
class SinglyNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next: SinglyNode | None = None


class LinkedList:
    def __init__(self) -> None:
        self.root = SinglyNode()

    def insert(self, data) -> None:
        cur = self.root
        while cur.next:
            cur = cur.next
        cur.next = SinglyNode(data)

    def search(self, target) -> bool:
        cur = self.root
        while cur.next:
            cur = cur.next
            if cur.data == target:
                return True
        return False

    def traverse(self) -> None:
        cur = self.root
        while cur.next:
            cur = cur.next
            print(cur.data)

    def update(self, target, new_value) -> None:
        cur = self.root
        while cur.next:
            cur = cur.next
            if cur.data == target:
                cur.data = new_value
                return

    def delete(self, target) -> None:
        cur = self.root
        last = cur
        while cur.next:
            last = cur
            cur = cur.next
            if cur.data == target:
                last.next = cur.next


# Doubly Linked List File
class DoublyNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.root = DoublyNode()

    def insert(self, value):
        cur = self.root
        while cur.next:
            cur = cur.next
            if cur == self.root:
                break
        cur.next = DoublyNode(value)
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

# Algorithms
