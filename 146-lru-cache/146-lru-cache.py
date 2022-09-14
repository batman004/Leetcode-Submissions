# class for doubly linked list to keep track of LRU and MRU
class Node:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # maps key->Node
        self.cap = capacity
        self.right, self.left = Node(0,0), Node(0,0)
        # left -> <- right
        self.left.next, self.right.prev = self.right, self.left 

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev
    
    # insert at the right
    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next = right.prev = node
        node.next, node.prev = right, prev
        
            
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove node and insert again from right,
            # since it becomes MRU now
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key exists then value needs to be updated
        # so remove it 
        if key in self.cache:
            self.remove(self.cache[key])
            
        # update the linked list
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)