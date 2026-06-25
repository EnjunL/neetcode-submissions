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
        #First pass, create copies
        hashmap = {}
        cur=head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur=cur.next
        
        #Second pass, add next and randoms
        #reset cur to front
        cur=head
        while cur:
            # for ex: setting hashmap["A"] => A' next node
            # to hashmap.get(A.next) which would be for ex: hashmap.get(C) => C'
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur = cur.next
        
        return hashmap.get(head)


        