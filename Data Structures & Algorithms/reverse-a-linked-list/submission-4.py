# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iterative Time: O(N) Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev        

#Recursive Time: O(N) Space: O(N)
#base case is null

        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            #revserse link btwn next node and head
            head.next.next = head
        head.next = None
        return newHead