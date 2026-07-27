class ListNode:
    def __init__(self,value):
        self.value = value
        self.prev = self.next = None
class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.right.prev, self.left.next = self.left, self.right
        #maps every value to the node so we can access in constant time
        self.map={}
    def length(self):
        return len(self.map)
        
    #insert from left remove from right

    def insert(self,val):
        node = ListNode(val)
        node.prev = self.left
        node.next = self.left.next

        self.left.next.prev = node
        self.left.next = node

        self.map[val] = node

    def pop(self,val):
        if val in self.map:
            node = self.map[val]
            #unlink our node from current connections
            node.next.prev = node.prev
            node.prev.next = node.next

            self.map.pop(val)

    def popRight(self):
        if not self.map:
            return None
        res = self.right.prev.value
        self.pop(res)
        return res

    def update(self, val):
        self.pop(val)
        self.insert(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCount = 0
        self.valMap = {} #map key to val
        self.countMap = collections.defaultdict(int) #map key to count
        self.listMap= collections.defaultdict(LinkedList) #map count of key to linkedlist

    def counter(self, key):
        count = self.countMap[key]
        self.countMap[key]+=1
        self.listMap[count].pop(key)
        self.listMap[count+1].insert(key)

        # is our count(the key's old freq) part of the lowest freq group? 
        # and after popping, is that group empty?
        # if so, lets move the lowest freq group up by 1
        if count == self.lfuCount and self.listMap[count].length()==0:
            self.lfuCount+=1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        #we dont need this since capacity is at least 1
        '''if self.cap==0:
            return'''
        #if at this point the key is not in the value map and capacity is full, evict
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCount].popRight()
            self.valMap.pop(res)
            self.countMap.pop(res)


        self.valMap[key] = value
        self.counter(key)
        self.lfuCount = min(self.lfuCount, self.countMap[key])

        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)