class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data) -> None:
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self) -> int:
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self) -> None:
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index: int):
        cur_idx = 0
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
        return

    def insert(self, data, index: int) -> None:
        cur = self.head
        cur_index = 0
        while cur.next != None:
            cur = cur.next
            last_node = cur.data  # 0
            if cur_index == index:
                cur.data = data  # inserted value
                temp = cur.next
                new_node = Node(last_node)
                cur.next = new_node
                new_node.next = temp
                return
            cur_index += 1
        new_node = Node(data)
        cur.next = new_node
        return

    def erase(self, index: int) -> None:
        cur_idx = 0
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1
        print('index out of range')
        return

    def clear(self):
        self.head = None


myList = LinkedList()
myList.display()
myList.append(1)
myList.append('2')
myList.append(3)
myList.append(4)
myList.display()
myList.insert(55, 1)
myList.display()
# myList.erase(1)
# myList.display()
