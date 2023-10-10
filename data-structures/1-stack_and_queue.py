class Stack:
    def __init__(self, max_size=None):
        self.stack = []*max_size
        self.size = 0
        self.max_size = max_size

    def __str__(self) -> str:
        return f'Stack: {self.stack}'

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.max_size else False

    def push(self, data):
        if self.isFull:
            return 'can\'t push more items'
        else:
            self.stack.append(data)
            self.size += 1

    def pop(self):
        if not self.isEmpty:
            self.stack.pop()
            self.size -= 1
        else:
            return 'the stack is empty'


class Queue:
    def __init__(self, max_size=None):
        self.queue = []
        self.size = 0
        self.max_size = max_size

    def __str__(self) -> str:
        return f'Queue: {self.queue}'

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.max_size else False

    def push(self, data):
        if not self.isFull():
            return self.queue.append(data)
        else:
            return 'No space left'

    def pop(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return 'No items left'


myQueue = Queue()
myQueue.push(12)
myQueue.push(15)
myQueue.push(18)
myQueue.push(19)
print(myQueue)
