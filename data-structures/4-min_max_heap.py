import sys


class MaxHeap:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.Heap = [0]*(self.max_size+1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos//2

    def left_child(self, pos):
        return (2*pos) + 1

    def right_child(self, pos):
        return (2*pos) + 2

    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, rpos):
        self.Heap[fpos], self.Heap[rpos] = self.Heap[rpos], self.Heap[fpos]

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[pos] < self.Heap[self.left_child(pos)] or self.Heap[pos] < self.Heap[self.right_child(pos)]:
                if self.Heap[self.left_child(pos)] > self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.maxHeapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.maxHeapify(self.right_child(pos))

    def insert(self, element: int):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped

    def printHeap(self):
        for i in range(1, (self.size//2) + 1):
            print(
                f'Parent: {self.Heap[i]} Left Child: {self.Heap[2*i+1]} Right Child: {self.Heap[2*i+2]}')


if __name__ == '__main__':
    print('The maxHeap is:')
    myMaxHeap = MaxHeap(max_size=20)
    myMaxHeap.insert(element=5)
    myMaxHeap.insert(3)
    myMaxHeap.insert(15)
    myMaxHeap.insert(18)
    myMaxHeap.insert(19)
    myMaxHeap.insert(28)
    myMaxHeap.insert(53)
    myMaxHeap.insert(27)
    myMaxHeap.insert(98)
    myMaxHeap.insert(9)
    myMaxHeap.printHeap()
    print(f'The Max Value in my Max Heap is: {myMaxHeap.extractMax()}')
    myMaxHeap.printHeap()
