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
        
        oldToCopy = { None : None } # old node -> copy node
        
        curr = head
        
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
            
        print(oldToCopy)    
        curr = head
        # set pointers in copied LL
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        return oldToCopy[head]
        
        