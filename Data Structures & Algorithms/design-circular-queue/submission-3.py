class ListNode:
    def __init__(self,val,nxt,prev):
        self.val,self.next,self.prev = val,nxt, prev
class MyCircularQueue:

    def __init__(self, k: int):
        #Left dummy node is the left border of the problem (front)
        #Right dummy node is right border of the problem (back)
        self.space = k
        self.left=ListNode(0,None,None)
        self.right=ListNode(0,None,self.left) 
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        #can only add value if there is enough space
        if self.isFull():
            return False
        cur = ListNode(value,self.right,self.right.prev)
        #update previous ptr (left of cur)
        self.right.prev.next = cur
        #update right of cur
        self.right.prev = cur
        self.space-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        #update the next and prev ptrs of the node we are dequeing

        #set left's next node to one more ahead to skip the next node
        self.left.next = self.left.next.next
        #set left's next's previous to skip the left's next node, and just link back to left itself.
        self.left.next.prev=self.left
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
        return self.left.next==self.right

    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()