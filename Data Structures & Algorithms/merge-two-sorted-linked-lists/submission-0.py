# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy head, and have a cur value for current node

        #iterate both nodes at the same time, and check which one is smaller, and stay on that node
        #stay until no longer smaller and switch to other node
        #add each smaller value to cur.next and update cur

        #return head of res 

        dummy = ListNode(0)
        cur = dummy
        #compares when both list have nodes
        while list1 and list2:
            if list1.val < list2.val:
                # attach node to merged list
                cur.next = list1
                list1=list1.next
            else:
                cur.next = list2
                list2=list2.next
            #move up the newly attached node
            cur=cur.next
        cur.next = list1 if list1 else list2
        return dummy.next

