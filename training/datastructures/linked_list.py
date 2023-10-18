class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, data) -> None:
        cur = self.root
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

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


if __name__ == '__main__':
    myLL = LinkedList()
    myLL.insert(15)
    myLL.insert(16)
    myLL.insert(17)
    myLL.insert(18)
    myLL.traverse()
