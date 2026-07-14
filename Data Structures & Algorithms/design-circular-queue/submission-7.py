class ListN:
    def __init__(self, val,prev,nxt):
        self.val = val
        self.prev = prev
        self.next = nxt
class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListN(0,None,None)
        self.right = ListN(0,self.left,None)#has a previous bc we just initialized 
        #since we just created right too, lets set left node's next
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur = ListN(value,self.right.prev,self.right)
        #connect new node to last node in line
        self.right.prev.next = cur
        #connect new node to the right dummy node
        self.right.prev = cur
        self.space-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        nxt = self.left.next.next
        self.left.next = nxt
        self.left.next.prev = self.left
        self.space+=1
        return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space==0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()