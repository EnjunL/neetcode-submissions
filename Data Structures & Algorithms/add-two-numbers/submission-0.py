# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy = ListNode(0)
        cur=dummy

        #also check if carry is non-null 
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            
            #new digit
            s = x+y+carry

            # what if we have 15:

            #gets the 1
            carry = s//10
            #gets the 5
            s = s%10

            cur.next = ListNode(s)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            cur=cur.next
        
        return dummy.next
        