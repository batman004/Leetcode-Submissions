# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head.next
        
        # this loop gets slow to middle element
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
        
        # now slow.next point to start of second half
        
        # we need to reverse second half of the LL and place the nodes between elements of the first half
        
        # 1->2->3->4->5->NULL
        
        # 1->2->3 || 4->5 
        
        # 1->2->3 || 5->4
        
        # 1->5->2->4->3->NULL
        
        second = slow.next
        slow.next = None # cut-off
        
        # reversing 2nd half
        prev = None
        while second:
            # store next node in temp
            temp = second.next
            
            # since we are reversing, point the next to prev
            second.next = prev
            
            prev = second
            
            # incerement the pointers
            
            prev = second
            
            second = temp
            
            
            
        # merging
        
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            
            second.next = tmp1
            
            first, second = tmp1, tmp2
        
        
        