#2ptr
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.front=0
        self.back=0
        self.size = 0
        self.capacity=k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.back] = value
        self.back = (self.back+1) % self.capacity #% helps wrap around
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.front] = None
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        #back is the empty slot, we want the thing before it so use modulo to get the previous for all cases
        if self.isEmpty():
            return -1
        return self.arr[(self.back-1) %self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()