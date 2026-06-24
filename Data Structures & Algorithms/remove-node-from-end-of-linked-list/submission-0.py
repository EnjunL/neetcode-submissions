# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) # create dummy node
        left = dummy
        right = head# n is our offset
        while n>0 and right:
            right = right.next
            n-=1
        #once n == 0, we have shifted enoguh

        while right:
            left = left.next
            right=right.next
        
        #delete node
        left.next = left.next.next

        return dummy.next
