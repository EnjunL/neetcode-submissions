# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #merge two list
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        dummy = head

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

        dummy.next = list1 if list1 else list2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #for loop from first list to last
        #init with a dummy node
        #each iteration, we merge the already sorted linked lists with our dummy node 
        #(the easy sorting problem)
        head = ListNode(0)
        dummy = head
        for i in range(len(lists)):
            dummy.next = self.mergeTwoLists(dummy.next, lists[i])
        return head.next
    