class DoublyLinkedNode:
    def __init__(self, key, value, prev, nxt):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        #init doubly linked list for usage order
        self.left = DoublyLinkedNode(0,0,None,None)
        self.right = DoublyLinkedNode(0,0,self.left,None)
        self.left.next = self.right
        self.space=0
        self.maxSpace=capacity
    

        #init a hashmap to store values
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        #get the node associated with our key
        current = self.cache[key]
        #swap out connections that were next to our node, find node first, then swap
        current.prev.next = current.next
        current.next.prev = current.prev
        #swap out connections to put our node to the front
        current.next = self.left.next
        current.prev = self.left

        self.left.next.prev = current
        self.left.next = current

        return current.value

    def put(self, key: int, value: int) -> None:
        #if key already exists, remove old node first
        if key in self.cache:
            old = self.cache[key]

            old.prev.next = old.next
            old.next.prev = old.prev

            self.cache.pop(old.key)

            self.space-=1

        #if space is full, remove oldest node
        if self.space >= self.maxSpace:
            old = self.right.prev

            old.prev.next = old.next
            old.next.prev = old.prev

            self.cache.pop(old.key)

            self.space-=1

        #create new node bc old node has same key but diff value
        node = DoublyLinkedNode(key,value,None,None)

        #insert new node at the front
        node.prev = self.left
        node.next = self.left.next

        self.left.next.prev = node
        self.left.next = node

        #store the new node
        self.cache[key] = node
        self.space+=1
        


        
