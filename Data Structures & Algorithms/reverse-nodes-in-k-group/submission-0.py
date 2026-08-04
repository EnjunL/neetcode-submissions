# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #point each forward connection backwards
    def getKthNode(self,head,k):
        current = head
        while current and k>0:
            current=current.next
            k-=1
        return current

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        #one node right before our loop
        groupPrev = dummy        
        while True:
            kth = self.getKthNode(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next

            #reverse group
            prev,curr = kth.next,groupPrev.next 
            # prev: old first element points at the old last element's next node, to not break the     connection to the next group of k nodes
            # curr: starting after the previous k nodes (the next spot after their end)
            while curr is not groupNext:
                nx = curr.next
                curr.next = prev
                prev = curr
                curr = nx

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next






