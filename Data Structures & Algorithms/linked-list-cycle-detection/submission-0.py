# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #ptrA has it in the beginning
        #ptrB has it ahead, and keeps checking if .next is ptrA
        #if so return T, else move ptrA, once ptrA==ptrB, return False

        A = head
        B = head
        while B and B.next:
            A=A.next
            B=B.next.next

            if A == B:
                return True
        return False