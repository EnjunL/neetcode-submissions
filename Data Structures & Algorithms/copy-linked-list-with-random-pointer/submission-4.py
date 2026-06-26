"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap={}

        cur=head
        #init deep copies
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        
        cur=head
        while cur:
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur=cur.next
        
        return hashmap.get(head)