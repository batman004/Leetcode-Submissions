class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        
        while True:
            
            # assume given array is LL and each value is pointer 
            # 0 1 2 3 4
            # 1 3 4 2 2
            
            # 1->3->2->4->2
            
            slow = nums[slow]
            
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
        slow2 = 0
        
        while True:
            
            slow2 = nums[slow2]
            
            slow = nums[slow]
            
            if slow == slow2:
                return slow