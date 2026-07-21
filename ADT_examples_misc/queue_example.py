class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0
    def isFull(self):
        return self.count == self.size
    def isEmpty(self):
        return self.count == 0
    def enqueue(self, element):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.queue[self.rear] = element
            self.count += 1
            print("Added:", element)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            element = self.queue[self.front]
            self.front += 1
            self.count -= 1
            print("Removed:", element)
            return element
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

Queue = Queue(5)
Queue.enqueue("A")
Queue.enqueue("B")
Queue.enqueue("C")
Queue.enqueue("D")
Queue.peek()
Queue.dequeue()
Queue.peek()