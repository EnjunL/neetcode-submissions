# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #check when left is reached, start reversing until we reach right
        #have a ptr always at the start of the linked list
        dummy = ListNode(0,head)

        #1) iterate until we reach the node before left (hence left-1)
        leftPrev,cur = dummy,head
        for _ in range(left-1):
            leftPrev,cur=cur,cur.next
        
        #2) reverse until we reach the end (R-L+1 to get the last right node)
        prev=None
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = prev
            prev,cur=cur,nxt
        
        #3) reconnect nodes: 
        #have original left node point at the node after original right node
        leftPrev.next.next = cur
        #have original right node be at the front of the reversed section
        leftPrev.next = prev

        return dummy.next





        