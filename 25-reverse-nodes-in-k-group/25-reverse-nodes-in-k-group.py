# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def getKth(curr, k):
            while curr and k>0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0, head)
        
        groupPrev = dummy
        
        while True:
            
            # get to Kth node
            kth = getKth(groupPrev, k)
            # basically we have come to the end of the LL
            if not kth:
                break
        
            groupNext = kth.next
            
            # reverse the group
            
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                
                # moving ptr ahead
                curr = tmp
                
            tmp = groupPrev.next
            
            groupPrev.next = kth
            
            groupPrev = tmp
            
        return dummy.next
                
                
                
            
            