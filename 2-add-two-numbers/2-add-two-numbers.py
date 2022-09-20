# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        
        cur = dummy
        
        # init carry to 0
        # iterate if l1/l2/carry exits
        # edge case 8 + 7 = 15. so LL shold be 1 -> 5
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            res = val1 + val2 + carry # if carry exists

            carry = res // 10
            
            res = res % 10 # only keep first digit if its > 10

            
            cur.next = ListNode(res)
            
            # shift pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
            
        return dummy.next
            
        
        
        