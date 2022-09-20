# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # dummy -> 1 -> 2 -> 3 -> 4 -> 5
        
        dummy = ListNode(0, head)
        left= dummy
        right = head
        
        # postition right ptr at distance of n from head
        
        while n > 0 and right:
            
            right = right.next
            n -= 1
            
        # shift left and right pointers
        # until right is None
        while right:
            left = left.next
            right = right.next
            
        # delete node 
        
        left.next = left.next.next
        
        return dummy.next